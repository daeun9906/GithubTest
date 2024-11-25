import googletrans
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic #QT dsesigner에서 만든 UI 호출 모듈



# 호출 식
form_class = uic.loadUiType("UI/googleTranslator.ui")[0]


class GoogleTransApp(QMainWindow, form_class):
    def __init__(self):
        super().__init__()    #부모 클래스 생성자 호출
        self.setupUi(self)    # 호출한 UI 연결


        self.setWindowTitle("Google Translator")
        self.setWindowIcon(QIcon("UI/googleIcon.png"))


        # 상태표시줄
        self.statusBar().showMessage("Google Translator v1.0")


        # 번역
        self.transButton.clicked.connect(self.transExectue)


    # 번역 메소드 생성
    def transExectue(self):
        korEdit = self.korEdit.text()      # 해당 line edit에 입력된 텍스트 호출


        # # 번역 객체 생성
        trans = googletrans.Translator()
        resultEng = trans.translate(korEdit, dest="en")
        resultJa = trans.translate(korEdit, dest="ja")


        self.engTrans.append(resultEng.text)
        self.jaTrans.append(resultJa.text)


app = QApplication(sys.argv)

googlewin = GoogleTransApp()
googlewin.show()
sys.exit(app.exec_())