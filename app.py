from flask import Flask, request, jsonify,  render_template
from flask_cors import CORS, cross_origin
import requests


from pymongo import MongoClient

import requests
import json

app = Flask(__name__)

CORS(app, resources={r'/*': {"origins": "*"}})

conn = MongoClient('mongodb://localhost:27017')
db = conn['dataset']
coll = db['parsed']


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/outro')
def hello():
    return "Hello client "


@app.route('/parse', methods=['POST'])
def extract():
    text = request.get_json(force=True)
    payload = json.dumps({
        "text": text['text']
    })
    headers = {
        'content-type': 'application/json'

    }
    response = requests.request(
        "POST", "http://localhost:5005/model/parse", headers=headers, data=payload)
    return response.json()


@app.route('/process', methods=['GET', 'POST'])
def process():
    text = request.get_json(force=True)
    # payload = {
    #	"message": "/start"
    #	}
    # headers = {
    # 'Content-type': 'application/json'

    # }
    #response = requests.request("POST", "http://localhost:5005/webhooks/rest/webhook", headers=headers, data={"message":"/start"} )
    r = requests.post('http://localhost:5005/webhooks/rest/webhook', verify=False,
                      data=json.dumps(
                          {"sender": "556198002190", "message": text['message']}),
                      headers={'Accept': 'application/json', 'Content-Type': 'application/json'})

    r.encoding = 'utf-8-sig'
    resposta = json.loads(r.text)
    resposta_final = ''
    for x in resposta:
        for y in x.keys():
            if y != 'text':
                continue
            resposta_final += (x['text']) + '\n'

    return jsonify({"valor": resposta_final})


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5056, use_reloader=True)
