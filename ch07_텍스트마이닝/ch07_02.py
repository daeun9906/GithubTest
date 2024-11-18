# TF-IDF 기반 벡터화
# 값이 높다고 무조건 중요한 단어는 아니기 때문에 범용 단어는 가중치 둬서 구분

from collections import Counter

from lxml.html.diff import token
from nltk import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer


text2 = ["I am a elementary school student.", "And I am a boy"]

txtTfid = TfidfVectorizer().fit(text2)
txtTfid_array = txtTfid.transform(text2).toarray()

print(txtTfid_array)
print(txtTfid.vocabulary_)