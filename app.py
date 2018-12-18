from flask import Flask, abort, request
import json

from algorithm import predict

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Auto Flask Dockerized'

@app.route('/analyze', methods=['POST'])
def analyze_request():
	if not request.json:
		abort(400)
	print(request.json)
	data_result = predict(request.json['id'])
	return str(data_result)

@app.route('/foo', methods=['GET', 'POST'])
def foo():
	return 'Reached'


if __name__ == "__main__":
	app.run(host='0.0.0.0')
