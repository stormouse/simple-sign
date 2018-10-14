from google.cloud import language
# import gensim
import numpy as np
# import requests
import gensim
import os
client = language.LanguageServiceClient()

# Load Google's pre-trained Word2Vec model.
cwd = os.getcwd()
model = gensim.models.KeyedVectors.load_word2vec_format(cwd + './model/GoogleNews-vectors-negative300.bin', binary=True)  

url = 'http://localhost:12345/word2vec'

valid_words_f = open('./backend/nlp/valid_words.txt', 'r')
valid_words = {k:1 for line in valid_words_f for k in line.split(',')}
valid_words_f.close()
# valid_vectors = list(map(lambda x : np.sum(requests.post(url, data = {'s':x}).json(), axis=1), valid_words.keys()))
#valid_vectors = list(map(lambda x : np.sum(requests.post(url, data = {'s':x}).json(), axis=1), valid_words.keys()))
valid_vectors = []
for w in valid_words.keys():
    vec = [model[x] for x in w.split() if x in model.wv.vocab]
    valid_vectors.append(np.sum(vec, axis=0) if len(vec) > 0 else np.zeros(len(valid_vectors[0])))
