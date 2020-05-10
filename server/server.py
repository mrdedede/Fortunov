from flask import Flask
from flask_cors import CORS
import produce

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def index():
    return "Hello, World!"

@app.route('/language/<language>', methods=['GET'])
def get_language_phrase(language):
    result = produce.produce_phrases(language)
    return result

app.run('127.0.0.1', 5000)