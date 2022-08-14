# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 12:15:25 2022

@author: Manpreet Kour
"""

import tensorflow as tf 
model = tf.keras.models.load_model('fake_news.h5')

class Predict:
    
    def predict_fake_news(self, score):
        return 1 if score>0.5 else 0
    
    def prediction(self, x_test_padded):
         score = model.predict(x_test_padded)
         result=self.predict_fake_news(score)
         return result