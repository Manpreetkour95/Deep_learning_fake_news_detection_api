# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 12:01:10 2022

@author: Manpreet Kour
"""

#!/usr/bin/env python
# encoding: utf-8
from flask import Flask, request, jsonify
from preprocessing import PreProcessing
from predict import Predict
from databaseConnect import DataBaseConnection


import logging 

app = Flask(__name__)


@app.route('/fake_news', methods=['POST']) 
def fake_news():
    
    try:
        data = request.json
        title=data["title"]
        text=data["text"]
    
        
        x_test_padded=PreProcessing().preprocessing(title, text)
        logging.debug("successfully converted title and text into tokenizer and padded token")
        
        result=Predict().prediction(x_test_padded)
        logging.debug("successfully prediction output from model")
        
        if result ==1: 
            response={"news":"Fake news"}
            
        else:
            response={"news":"Not Fake news"}
            
        logging.debug("converted binary resonse into fake or not fake news")
        DataBaseConnection().push_to_db(text + ' ' + title, response)
        return jsonify(response)
    except Exception as e:
        logging.error(e)
        response={"news":"unable to predict"}
        return response
        
    
app.run(debug=True)