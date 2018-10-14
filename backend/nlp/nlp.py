#-*- coding:utf-8 -*-
from .. import nlp_app
from . import model, client, valid_words, valid_vectors
# from .model import model
from google.cloud import language
from google.cloud.language import enums, types
from flask import request
import numpy as np
# from sklearn.cluster import KMeans, SpectralClustering 
from gensim.utils import tokenize
import scipy, json
# import requests
import threading


nc = 3
threashold = 0.8
# clf = SpectralClustering(n_clusters=nc, affinity="precomputed")
url = 'http://localhost:12345/word2vec'


def similar_score(a, b):
    if np.count_nonzero(a) == 0 or np.count_nonzero(b) == 0:
        return 0
    return 1 - scipy.spatial.distance.cosine(a, b) 

def rough_filter(semaphore, response, words):
    global url, threashold
    semaphore.acquire()
    X = []
    for w in words:
        res = requests.post(url, data = {'s': w}).json()
        X.append(res[0])
    for i in X:
        sim_scores = []
        for j in range(len(valid_vectors)):
            sim_scores.append(similar_score(i, valid_vectors[j]))
        label = np.argmax(sim_scores)
        if sim_scores[label] > threashold:
            response.add(list(valid_words.keys())[label])
    semaphore.release()

# def extract_tag():


@nlp_app.route('/nlp',  methods=['POST'])
def nlp():
    global nc, url, threashold
    semaphore = threading.Semaphore(5)
    threads = []

    if request.method == 'POST':
        response = {'setions':[]}
        text = request.form['file']
        
        for pharases in text.split('\n'):
            sentences = pharases.lower().split('.')
            words = {item for s in sentences for item in list(tokenize(s))}
            rough_tags = set([])
            threads.append(threading.Thread(target=rough_filter,
                          args=(semaphore, rough_tags, words)))
            map(lambda t: t.start(), threads)
            current_valid, current_valid_vec = [], []
            for i, w in enumerate(valid_words.keys()):
                if w in words:
                    current_valid.append(w)
                    current_valid_vec.append(valid_vectors[i]) 
            print (current_valid)
            M = len(current_valid)
            tags = set([])
            if M > 0:
                document = types.Document(
                    content='.'.join([' '.join(list(tokenize(s))) for s in sentences]) + '.',
                    type=enums.Document.Type.PLAIN_TEXT)
                entities = client.analyze_entities(document).entities
                tmp = {e.name for e in entities}
                entities = list(tmp)
                X = []
                for e in entities:
                    # res = requests.post(url, data = {'s':e}).json()
                    # X.append(np.sum(res, axis=0) if len(res) > 0 else np.zeros(M))
                    vec = [model[w] for w in e.split() if w in model.wv.vocab]
                    X.append(np.sum(vec, axis=0) if len(vec) > 0 else np.zeros(len(valid_vectors[0])))
                sim_scores = np.zeros((len(entities),M))
                clusters = {i:[] for i in range(M)}
                for i in range(len(entities)):
                    for j in range(M):
                        sim_scores[i][j] = similar_score(X[i], current_valid_vec[j])
                    label = np.argmax(sim_scores[i])
                    if sim_scores[i][label] > threashold:
                        clusters[label].append(entities[i])
                tags = {current_valid[k] for k in range(M) if len(clusters[k]) > 0}
                print (tags, clusters.values())
            map(lambda t: t.join(), threads)
            triggers = tags.copy()
            triggers.update(rough_tags)
            response['setions'].append({'content':pharases,
                                        'triggers':  list(triggers) if len(triggers) > 0 else 'EVERY_TIME'})
            
            # for k, v in clusters.items():
            #     print (k, v)
        return json.dumps(response)
