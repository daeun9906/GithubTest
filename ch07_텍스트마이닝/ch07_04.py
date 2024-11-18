import json
import re
import pandas as pd
from ch07_텍스트마이닝.ch07_03 import tfidf, sa_lr_best

with open("./java/코로나_news.json", encoding= "utf-8") as j_f:
    data = json.load(j_f)


# 제목, 요약만 추출
data_title = []
data_description = []

for t in data:
    data_title.append(t['title'])
    data_description.append(t['description'])


# Df생성
data_df = pd.DataFrame({"title": data_title, "description": data_description})


# 텍스트 전처리(한글 제외한 문자 제거)
data_df["title"] = data_df["title"].apply(lambda x: re.sub(r'[^ㄱ-ㅣ가-힣]+', " ", x))
data_df["description"] = data_df["description"].apply(lambda x: re.sub(r'[^ㄱ-ㅣ가-힣]+', " ", x))


data_title_tfidf = tfidf.transform(data_df['title'])
data_description_tfidf = tfidf.transform(data_df['description'])


data_title_predict = sa_lr_best.predict(data_title_tfidf)
data_description_predict = sa_lr_best.predict(data_description_tfidf)


# 새로운 열 추가하기
data_df["title_label"] = data_title_predict
data_df["description_label"] = data_description_predict


# utf-8은 엑셀에서 깨짐
data_df.to_csv('java/코로나_뉴스_감성분석.csv', encoding="euc-kr")
















