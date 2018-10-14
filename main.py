from backend import nlp_app
from backend.nlp import nlp

if __name__ == '__main__':
    nlp_app.run(host='localhost', port='8080', debug = True)
