import googletrans

# 제공하는 언어의 딕셔너리. dest: eng, ja, zh-cn
# print(googletrans.LANGUAGES)



#구글 번역기 생성
trans = googletrans.Translator()

resultJa = trans.translate("안녕", dest = "ja")


print(f"일본어: {resultJa.text}")