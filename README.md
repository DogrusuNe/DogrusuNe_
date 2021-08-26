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

# Süreç
Literatürde birleşik ve ayrı yazımları karıştırılan kelimeler hakkında daha önce bir çalışma Türkçe’ de bulunmamaktadır. Bu kelimeler arasında anlamsal olarak yazım şekli değişenler olsada anlamsal olmayanları da sözlüğümüze dahil ettik. Bu şekilde 35657 tane kelime elde ettik. Bu kelimelerin yazımı genellikle karıştırılır ve yanlış kullanımı oldukça fazladır. Modelimizi oluştururken derin öğrenme algoritması olan BiLSTM ve makine öğrenimi algoritmalarından biri olan XGBoost algoritmaları denenmiştir. 

İki modeli denemeden önce ön işleme aşamasında verimizi geçirdik. Bu aşamada birleşik yazılan kelimeleri anlamlı bir şekilde parçaladık. Ardından yazımı karıştırılan sözlüğümdeki bütün kelimelerin aralarında birer boşluk bulunmuş oldu ve bu boşluklara ‘X’ yerleştirildi. Bunun ardında ayrı yazılan kelimelerden biri var ise cümlemizde bu cümle 0, bitişik yazılan kelimelerden biri var ise 1 olarak etiketlemeyi gerçekleştirdik. Modelin doğru bir şekilde öğrenebilmesi için random undersampling ile hata oranı azaltılmış oldu. Oluşturduğumuz bu yeni veri setinden test verisi için %20’lik kısmı, %80’lik kısmı ise modeli eğitmek için kullanıldı.

LSTM’ler uzun vadeli bağımlılık problemini çözmek için tasarlanan özel bir RNN türüdür (Hochreiter & Schmidhuber, 1997). Bilgiyi uzun süre hatırlama davranışı sergilerler. LSTM'ler tüm tekrarlayan sinir ağları gibi bir sinir ağının tekrar eden hücrelerine sahiptir, fakat tekrar eden hücre tek bir sinir ağı kapısına sahip olmak yerine, etkileşime giren 3 adet kapıya sahiptir(Graves & Schmidhuberab, 2005). BiLSTM'de tek bir modeli eğitmek yerine iki modeli eğitiyoruz. İlk model sağlanan girdinin sırasını öğrenir ve ikinci model bu sıranın tersini öğrenir.

Doğruluğu yüksek bir topluluk öğrenme modeli geliştirmek için ilk seviyede farklı tahminleme yöntemlerine sahip olan lojistik regresyon, extra ağaçlar, destek vektör makinesi algoritmaları kullanılmıştır. İkinci seviyede ise ağırlıklandırma yaparak birkaç modelin ortalamasıyla hatalı tahminlemeyi en aza indiren yükseltme algoritmalarından XGBoosting kullanılmıştır. İlk seviyede kullanılan algoritmalar ikinci seviyenin girdilerini oluşturarak performansı artırmaktadır.
Bu iki modelden en iyi performansı veren BiLSTM algoritmasıdır. Modelimizi bu algoritmayla oluşturduk. Ayrıca bu modeli web sitemizin arka planında kullandık.


## BiLSTM
<p align="center">
  <img width="600" src="https://user-images.githubusercontent.com/59619952/130865326-1c88d68e-2811-447a-979a-8dfd207f665a.PNG"/>
</p>




## XGBoost
<p align="center">
  <img width="600"  src="https://user-images.githubusercontent.com/59619952/130865045-65970735-735a-4360-bf65-ef697d458cf9.png"/>
</p>



# Gereklilikler

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
      
# Performans Sonuçları

## Bidirectional LSTM                                            
|               | Precision     | Recall        | F1 Score      |
| ------------- | ------------- | ------------- | ------------- |
| 0             | 0.9493        | 0.8679        | 0.9068        |
| 1             | 0.8783        | 0.9536        | 0.9144        |

Accuracy: 0.910752193340



##   XBGoost                                         
|               | Precision     | Recall        | F1 Score      |
| ------------- | ------------- | ------------- | ------------- |
| 0             | 0.73        | 0.74        | 0.73        |
| 1             | 0.75        | 0.73        | 0.73        |

Accuracy: 0.73

# DogrusuNe (Flask API)
<p align="center">
  <img src="https://user-images.githubusercontent.com/59619952/130865747-d43f4723-c45f-490b-bbf2-8ad3adfe1db7.PNG"/>
</p>


# Kaynakça
* Babüroğlu, Barış & Tekerek, Adem & Tekerek, Mehmet. (2019). Development of Deep Learning Based Natural Language Processing Model for Turkish. 
* Çürük, Yasemin. (2019). BİRLEŞİK SÖZCÜK MÜ ÖBEK Mİ?. 23. 255-2981. 
* Karacaoğlu, Mehmet Önder. (2010). BİRLEŞİK KELİMELERİN YAZIMI Yüksek Lisans Tezi. 

   


