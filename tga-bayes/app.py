#!/usr/bin/env python

import json
from flask import Flask, jsonify, request
from subprocess import Popen, PIPE

app = Flask(__name__)

@app.route("/")
def hello():
    return "Submit a POST to the /tga route"

@app.route("/tga", methods=['POST'])
def predict():
    data = request.get_json()
    
    process = Popen(['python', 'Run_Case.py', 'gypsum_5k', '1', '2'], stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()

    result = 1
    return jsonify(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
