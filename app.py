from flask import Flask, request, jsonify,  render_template
import requests


from pymongo import MongoClient

import requests
import json

app = Flask(__name__, template_folder= 'Templates')



conn = MongoClient('mongodb://localhost:27017')
db = conn['dataset']
coll = db['parsed']


@app.route('/')
def hello():
	return "Hello client "

@app.route('/parse', methods = ['POST'])
def extract():
	text = request.get_json(force=True)
	payload = json.dumps({
		"text": text['text']
		})
	headers = {
	'content-type': 'application/json'

	}
	response = requests.request("POST", "http://localhost:5005/model/parse", headers=headers, data=payload )
	return response.json()

if __name__ == '__main__':
  app.run(host='0.0.0.0' , debug = True, port= 5056, use_reloader = True )