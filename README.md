# DogrusuNe

![logo2-removebg-preview (1)](https://user-images.githubusercontent.com/59619952/130329449-6ccb622a-1247-4688-9680-81802eb7c83a.png)

# Amacımız

Türkçe birleşik kelimelerin yazımında hata bulan ve doğru kullanımını öneren bir uygulama sunmak. Geliştirdiğimiz bu uygulama ile günlük hayatta sıklıkla kullandığımız ve nadiren kullandığımız birleşik kelimelerin yazımındaki karışıklığı ortadan kaldırmayı hedefliyoruz. Özellikle bu konuya dikkat çekerek ve çözüm getirerek Türkçeye büyük katkı sağlayacağımızı düşünüyoruz.


# Takım Üyeleri

   *   Havvanur Bozömeroğlu (havvabzmr@gmail.com)
   *   Merve Korkut (korkutt98@gmail.com)
   *   Selin Gökcan (www.selin.gokcan@gmail.com)
   *   Selen Gökcan (gokcanselen@gmail.com) 





# Yöntem 

Bu proje boyunca kullandığımız araçlar ve yöntemleri aşağıda bulabilirsiniz.

## Veri seti

Kulllandığımız veri setine bu linkten erişebilirsiniz:
https://www.kaggle.com/mahdinamidamirchi/turkish-sentences-dataset

Veri seti Wikipedia'dan elde eldilen Türkçe kelimelerden oluşmaktadır. Her cümle en fazla 14, en düşük 2 kelimeden oluşur. Cümlelerin içerisinde herhangi bir özel karakter veya kısaltma bulunmuyor. Sürekli güncellenen bir veri setidir. Bizim kullandığımız versiyonda toplam 170458 satırdan oluşur. Yani içerisinde 170458 tane cümle bulundurur.

Ayrıca oluşturduğumuz küçük çaplı veri setleri bulunuyor.
* atasözleri.txt --> 2265 tane atasözü barındıran bir txt belgesidir.
* yaban yakup kadri karaosmanoğlu.txt --> Edebiyatımızda ünlü bir eser olan Yaban kitabının cümlelerinde oluşan bir txt belgesidir. 5169 satırdan oluşmaktadır.

## Sözlükler
* kelime_sözlüğü.txt -->  Genellikle birleşik ve ayrı yazımında hata yapılan kelimelerden oluşan sözlüktür. 35657 tane satırdan oluşmaktadır.
* ayrıyazılan.txt  -->  Ayrı yazılması gereken kelimelerden oluşan sözlüktür. 27219 tane satırdan oluşmaktadır.
* birlesikyazılankelimeler.txt -->  Birleşik yazılması gereken kelimelerden oluşan süzlüktür. 8801 tane kelimeden oluşmaktadır.

#Gereklilikler

* Model için  -->  Python 3.6+
* Web Sitesi için  -->  HTML, CSS, JavaScript, Bootstrap, Flask, Python 3.6+

## BiLSTM için Gerekli Kütüphaneler

      import pandas as pd
      import keras
      import pickle
      from keras.preprocessing.text import Tokenizer
      from keras.preprocessing.sequence import pad_sequences
      from sklearn.model_selection import train_test_split
      import tensorflow as tf
      from keras.layers import Dense, LSTM, Flatten, Embedding, Dropout , Activation, GRU, Flatten, Input, Bidirectional, GlobalMaxPool1D, Convolution1D, TimeDistributed, Bidirectional
      from keras.layers.embeddings import Embedding
      from keras.models import Model, Sequential
      from keras import initializers, regularizers, constraints, optimizers, layers
      
 ## XGBoost (Alternatif Model) için Gerekli Kütüphaneler
 
      import pandas as pd
      import numpy as np
      from sklearn import metrics
      import keras
      import pickle
      from keras.preprocessing.text import Tokenizer
      from keras.preprocessing.sequence import pad_sequences
      from sklearn.model_selection import train_test_split
      from vecstack import stacking
      from xgboost import XGBClassifier
      from sklearn.ensemble import ExtraTreesClassifier
      from sklearn.linear_model import LogisticRegression
      from sklearn.svm import SVC
      from sklearn.metrics import accuracy_score
      
## Web Sitesi için Gerekli Kütüphaneler
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
      import string
      import regex
      



# Kaynakça
   * https://github.com/rounakdatta/CorrectLy
   * https://towardsdatascience.com/develop-a-nlp-model-in-python-deploy-it-with-flask-step-by-step-744f3bdd7776
   * https://github.com/brolin59/trnlp


