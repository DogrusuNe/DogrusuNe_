import pickle
import os
from tensorflow.python.keras.preprocessing.text import Tokenizer
from tensorflow.python.keras.preprocessing.sequence import pad_sequences
from keras.models import load_model
from keras.models import Model, Sequential
import re
import tensorflow as tf
from keras.layers import Dense, LSTM, Flatten, Embedding, Dropout , Activation, GRU, Flatten, Input, Bidirectional, GlobalMaxPool1D, Convolution1D, TimeDistributed, Bidirectional
from keras.layers.embeddings import Embedding
from flask_wtf import FlaskForm
from flask import Flask, request, render_template,redirect
from wtforms.validators import DataRequired
import pandas as pd
from os.path import join

app = Flask(__name__)
app.config['SECRET_KEY'] = "DontTellAnyone"

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/predict', methods=['GET', 'POST'])
def predictt():
  if request.method == 'POST' and 'text_enter' in request.form:
    output = request.form['text_enter']
    output = correct(output)
    return render_template('index.html', prediction=output)
  return render_template('index.html')


@app.route('/predict2', methods=['GET', 'POST'])
def predicttword():
  if request.method == 'POST' and 'text_enter2' in request.form:
    output = request.form['text_enter2']
    with open("dogru_kelimeler.txt","r",encoding="utf-8") as f:
      dogru_kelimeler = [line.strip() for line in f]  
    with open("kelimeler.txt","r",encoding="utf-8") as f:
      kelimeler2 = [line.strip() for line in f]  

    liste5 = []
    for k in range(len(kelimeler2)):
      if kelimeler2[k] in output:
        liste5.append(dogru_kelimeler[k])
    words = ', '.join(liste5[0:])
    return render_template('index.html', prediction2=words)
  return render_template('index.html')

this_dir, this_filename = os.path.split('__file__')

def build_model(embedsize):
    model = Sequential()
    model.add(Embedding(15000, embedsize))
    model.add(Bidirectional(LSTM(64, return_sequences = True)))
    model.add(Bidirectional(LSTM(32, return_sequences = True)))
    model.add(GlobalMaxPool1D())
    model.add(Dense(1, activation="sigmoid"))
    return model

def check(text):
    tokenizerpath = os.path.join(this_dir, "tokenizers", "tokenizer_birlesik_ayri2.pickle")
    weigthpath = os.path.join(this_dir, "weights", "Model_birlesik_ayri2.h5")
    model = build_model(128)
    with open(tokenizerpath, 'rb') as handle:
        turkish_tokenizer = pickle.load(handle)
    model.load_weights(weigthpath)
    tokens = turkish_tokenizer.texts_to_sequences([text])
    tokens_pad = pad_sequences(tokens, maxlen=7)
    res = model(tokens_pad)
    
    return (res[0][0])


import string
import re
import regex


def text_split(text):
  PUNCT_RE = regex.compile(r'(\p{Punctuation})')   
  text_list = PUNCT_RE.split(text)
  text_sentence = []
  punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
  for i in range(len(text_list)):
      if text_list[i] not in punctuations :
        text_sentence.append(text_list[i])
        
  return text_sentence


def correct(text):
  
    
  with open("kelimeler_isaretlenmis.txt","r",encoding="utf-8") as f:
      isaret_kelimeler = [line.strip() for line in f]
  with open("kelimeler.txt","r",encoding="utf-8") as f:
      kelimeler = [line.strip() for line in f]  
  

  text_sentence = text_split(text)
  
  #cumleler = text_sentence[text_sentence[0].str.contains('|'.join(kelimeler))]

  #cumleler = text_sentence[~text_sentence[0].str.contains('|'.join(kelimeler))]
  cumleler = []
  for t in range(len(text_sentence)):
    for s in range(len(kelimeler)):
      if kelimeler[s] in text_sentence[t]:
        cumleler.append(text_sentence[t])
        break
  
  #cumleler = text_sentence[text_sentence[0].str.contains('|'.join(kelimeler))]
  for d in range(len(cumleler)):
    for k in range(len(kelimeler)):
      cumleler[d]= cumleler[d].replace(kelimeler[k], isaret_kelimeler[k]) 
  
  truth2 = []
  for i in range(len(cumleler)):

    if check(cumleler[i]) > 0.5: 
      liste = cumleler[i].split()
      for w in range(len(liste)):
        if liste[w] == 'X':
          word = liste[w-1] + liste[w+1]
          liste[w-1] = word
          del liste[w:w+2]
          break
      truth = ' '.join(liste[0:])
                        
    else:
      liste2 = cumleler[i].split()
      for l in range(len(liste2)):
        if liste2[l] == 'X':
          word2 = liste2[l-1] + ' ' + liste2[l+1]
          liste2[l-1] = word2
          del liste2[l:l+2]
          break
      truth = ' '.join(liste2[0:])
    truth2.append(truth)      
  
  
  truth3 = '. '.join(truth2[0:])
  return truth3                      




if __name__ == '__main__':
    app.run(debug=True)