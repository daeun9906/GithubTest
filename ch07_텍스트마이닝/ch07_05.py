import pandas as pd
from statsmodels.base.covtype import descriptions

from ch07_텍스트마이닝.ch07_04 import data_df

data_df = pd.read_csv('./java/코로나_뉴스_감성분석.csv', encoding='eud-kr')


negative_df = pd.DataFrame(columns=["title", "title_label", "description", "description_label"])
positive_df = pd.DataFrame(columns=["title", "title_label", "description", "description_label"])


# 1회전: 첫번째 행이 data에 저장(index=0), 2회전: 두번째 행이 data에 저장
# 행 단위로 움직임
for index, data in data_df.iterrows:
    title = data["title"]
    description = data["description"]
    title_label = data["title_label"]
    description_label = data["description_label"]
    if d_label == 0:  # 부정 감성만 추출
        NEG_data_df = pd.concat([NEG_data_df, pd.DataFrame([[title, t_label, description, d_label]],
                                                           columns=["title","title_label","description","description_label"])],
                                ignore_index=True)
    else:
        POS_data_df = pd.concat([POS_data_df, pd.DataFrame([[title, t_label, description, d_label]],
                                                           columns=["title", "title_label", "description",
                                                                    "description_label"])], ignore_index=True)



NEG_data_df.to_csv("data/코로나뉴스_NEGATIVE.csv", encoding="euc-kr")
POS_data_df.to_csv("data/코로나뉴스_POSITIVE.csv", encoding="euc-kr")


print(f"부정 감성 요약 뉴스 개수 : {len(NEG_data_df)}")
print(f"긍정 감성 요약 뉴스 개수 : {len(POS_data_df)}")



### 긍정 감성 뉴스명사 리스트 추출
POS_description = POS_data_df["description"]  # 긍정 요약 뉴스에서 description 칼럼만 추출
POS_description_noun_tk = []  # 명사만 추출하여 담길 빈 리스트

okt = Okt()

for des in POS_description:
    POS_description_noun_tk.append(okt.nouns(des))

print(POS_description_noun_tk)

POS_description_noun_join = []  # 1차원 리스트(모든 요소를 join)


for des in POS_description_noun_tk:
    POS_description_noun_temp = []
    for des2 in des:
        if len(des2) > 1:
            POS_description_noun_temp.append(des2)
    POS_description_noun_join.append(" ".join(POS_description_noun_temp))

print(POS_description_noun_join)



### 부정 감성 뉴스명사 리스트 추출
NEG_description = NEG_data_df["description"]  # 긍정 요약 뉴스에서 description 칼럼만 추출
NEG_description_noun_tk = []  # 명사만 추출하여 담길 빈 리스트

okt = Okt()


for des in NEG_description:
    NEG_description_noun_tk.append(okt.nouns(des))
print(NEG_description_noun_tk)


NEG_description_noun_join = []  # 1차원 리스트(모든 요소를 join)
for des in NEG_description_noun_tk:
    NEG_description_noun_temp = []
    for des2 in des:
        if len(des2) > 1:
            NEG_description_noun_temp.append(des2)
    NEG_description_noun_join.append(" ".join(NEG_description_noun_temp))


print(NEG_description_noun_join)