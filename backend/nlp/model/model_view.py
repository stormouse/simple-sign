from . import model_app, model
from flask import request
import json
import multiprocessing
import gensim
# from gensim.corpora.wikicorpus import WikiCorpus
# from gensim.models.word2vec import Word2Vec

# # word2vec = gensim.models.KeyedVectors.load_word2vec_format('./model/GoogleNews-vectors-negative300.bin', binary=True)

# wiki = WikiCorpus('./model/swwiki-latest-pages-articles.xml.bz2', 
#                   lemmatize=False, dictionary={})
# sentences = list(wiki.get_texts())
# params = {'size': 500, 'window': 10, 'min_count': 10, 
#           'workers': 1, 'sample': 1E-3,}
# word2vec = Word2Vec(sentences, **params)

@model_app.route('/word2vec',  methods=['POST'])
def word2vec():
    if request.method == 'POST':
        s = request.form['s']
        return json.dumps([model[w].tolist() for w in s.split() if w in model.wv.vocab])
