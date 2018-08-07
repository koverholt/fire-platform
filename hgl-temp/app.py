#!/usr/bin/env python

import json
from flask import Flask, jsonify, request
from hgl_temp import predict_hgl

app = Flask(__name__)

@app.route("/")
def hello():
    return "Submit a POST to the /hgl route"

@app.route("/hgl", methods=['POST'])
def predict():
    data = request.get_json()
    result = predict_hgl(**data)
    return jsonify(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)