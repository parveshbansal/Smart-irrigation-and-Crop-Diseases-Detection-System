#main.py
import base64
#from flask import jsonify,request,Flask
import numpy as np
from PIL import Image
from imageai.Prediction.Custom import CustomImagePrediction
import os
execution_path = os.getcwd()
from flask import Flask
from flask import url_for, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.php')
@app.route('/foo', methods=['POST'])
def foo():
    a=[]
    prediction= CustomImagePrediction()
    prediction.setModelTypeAsResNet()
    prediction.setModelPath("model_ex-030_acc-0.996974.h5")
    prediction.setJsonPath("model_class2.json")
    prediction.loadModel(num_objects=13)
    predictions, probabilities = prediction.predictImage("images/image.jpg", result_count=3)
    for eachPrediction, eachProbability in zip(predictions, probabilities):
        #print(eachPrediction , " : " , eachProbability)
        a.append(eachPrediction)
    return jsonify({"Your image result is here and solution has been sent via a mail": a[0]})
if __name__ == "__main__":
    app.run(port=8080, debug=True)
