# 카운트 기반 벡터화
# 단어 피처에 숫자형 값을 할당
# 문서별 단어 빈도를 정리하기 위해서. 출현 빈도가 높을수록 중요한 단어


from collections import Counter

from lxml.html.diff import token
from nltk import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

text = [
    "I am a elementary student",
    "And I am a boy"
]



# 토큰화, 중첩 리스트 형태.
tokenList = []
for txt in text:
    tokenList.append(word_tokenize(txt))


print(f"토큰화 리스트: {tokenList}")



# 단어 빈도수 측정
str_counter = Counter()
for txt in tokenList:
    str_counter.update(txt)

print(f"단어 빈도수 측정: {str_counter}")



# 중복 제거. 딕셔너리 형태라 키값만 빼오면 중복 제거됨
onlytokenList = []
for k, v in str_counter.items():
    onlytokenList.append(k)


print(f"중복 제거 리스트: {onlytokenList}")




str_counter_vector = []

for str in onlytokenList:
    str_vector = []

    for word in str:
        str_vector.append(str_counter[word])

    str_counter_vector.append(str_vector)

print(str_counter_vector)




#
text2 = ["I am a elementary school student. And I am a boy"]
txt_vector = CountVectorizer()
txt_vector_arry = txt_vector.fit_transform(text2).toarray()
print(f"텍스트 벡터를 1차원 배열로: {txt_vector_arry}")
print(txt_vector.vocabulary_)




TfidfVectorizer.fit(text2)






