from flask import Flask
import gensim
# from gensim.corpora.wikicorpus import WikiCorpus
# from gensim.models.word2vec import Word2Vec

# model = gensim.models.KeyedVectors.load_word2vec_format('./backend/nlp/model/GoogleNews-vectors-negative300.bin', binary=True)
model = gensim.models.KeyedVectors.load_word2vec_format('./model/GoogleNews-vectors-negative300.bin', binary=True)

# wiki = WikiCorpus('./model/swwiki-latest-pages-articles.xml.bz2', 
#                   lemmatize=False, dictionary={})
# sentences = list(wiki.get_texts())
# params = {'size': 500, 'window': 10, 'min_count': 10, 
#           'workers': 1, 'sample': 1E-3,}
# model = Word2Vec(sentences, **params)
model_app = Flask(__name__)
