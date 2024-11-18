# 경고 제거
import warnings
warnings.filterwarnings(action="ignore")

import re
from konlpy.tag import Okt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score
import pandas as pd

# 데이터 로드
train_data = pd.read_csv("ratings_train.txt", encoding='utf-8', sep="\t", engine='python')
test_data = pd.read_csv("ratings_test.txt", encoding='utf-8', sep="\t", engine='python')

# 결측치 제거
train_data = train_data[train_data["document"].notnull()]
test_data = test_data[test_data["document"].notnull()]

# 한글만 남기기
train_data["document"] = train_data["document"].apply(lambda x: re.sub(r'[^ㄱ-ㅣ가-힣]+', " ", x))
test_data["document"] = test_data["document"].apply(lambda x: re.sub(r'[^ㄱ-ㅣ가-힣]+', " ", x))

# 형태소 분석기
okt = Okt()
def okt_tokenizer(text):
    tokens = okt.morphs(text)
    return tokens

# TfidfVectorizer
tfidf = TfidfVectorizer(tokenizer=okt_tokenizer, min_df=3, max_df=0.9, ngram_range=(1, 2))
tfidf.fit(train_data["document"])
train_tfidf = tfidf.transform(train_data["document"])

# 회귀 모델 생성
sa_lr = LogisticRegression(random_state=0, max_iter=500)
sa_lr.fit(train_tfidf, train_data["label"])

# 하이퍼파라미터 튜닝
params = {"C": [1, 3, 3.5, 4, 4.5, 5]}
sa_lr_grid_cv = GridSearchCV(sa_lr, param_grid=params, cv=3, scoring="accuracy", verbose=1)
sa_lr_grid_cv.fit(train_tfidf, train_data["label"])

# 최적 모델 저장
sa_lr_best = sa_lr_grid_cv.best_estimator_

# 모델 평가
test_tfidf = tfidf.transform(test_data["document"])
test_predict = sa_lr_best.predict(test_tfidf)
model_accuracy = accuracy_score(test_data["label"], test_predict)
print(f"감성 분석 모델 정확도: {round(model_accuracy, 4) * 100}%")

# 사용자 입력 테스트
txt = "웃자웃자~ 2024년 12월 시작~ 앗싸~! 좋은 예감! 난 잘될놈!"
txt = re.sub(r"[^ㄱ-ㅎㅏ-ㅣ가-힣]+", " ", txt)
txt = [txt]

txt_tfidf = tfidf.transform(txt)
txt_predict = sa_lr_best.predict(txt_tfidf)

print("=========================================================")
if txt_predict == 0:
    print("입력하신 문장은 부정 감성입니다.")
else:
    print("입력하신 문장은 긍정 감성입니다.")
