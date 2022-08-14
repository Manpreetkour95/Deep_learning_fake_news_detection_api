# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 12:03:54 2022

@author: Manpreet Kour
"""

#from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')


w_tokenizer = nltk.tokenize.WhitespaceTokenizer()
lemmatizer = nltk.stem.WordNetLemmatizer()
stop = stopwords.words('english')

# loading
import pickle
with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)
    
class PreProcessing:
    def __init__(self):
        self.max_length=12468
        self.truc_type="post"
        

    def lemmatize_text(self, text):
        return [lemmatizer.lemmatize(w) for w in w_tokenizer.tokenize(text)]
    
    
    def preprocessing(self,title, text):
        
        title_text=title+" "+text
        
        ### covert to lowercase
        title_text=title_text.lower()
        
        ### removing special characters 
        title_text=title_text.replace("n't"," not")
        title_text=title_text.replace('\W', ' ')
        
        ### stopwords removal 
        title_text =' '.join([word for word in title_text.split() if word not in (stop)])
    
        ### Lemmatization 
        title_text=self.lemmatize_text(title_text)
        title_text=' '.join(title_text)
            
        test_sequences=tokenizer.texts_to_sequences([title_text])
        
        x_test_padded=pad_sequences(test_sequences, maxlen=self.max_length, truncating=self.truc_type)
        
        return x_test_padded