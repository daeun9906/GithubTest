import googletrans
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic #QT dsesigner에서 만든 UI 호출 모듈

from os import environ
import multiprocessing as mp



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

        # 초기화
        self.resetButton.clicked.connect(self.transReset)


    # 번역 메소드 생성
    def transExectue(self):
        korEdit = self.korEdit.text()      # 해당 line edit에 입력된 텍스트 호출

        # 공백 입력
        if korEdit == "":
            QMessageBox.warning(self,"입력오류", "You Must Text Something.")

        else:
            # 번역 객체 생성
            trans = googletrans.Translator()
            resultEng = trans.translate(korEdit, dest="en")
            resultJa = trans.translate(korEdit, dest="ja")

            self.engTrans.append(resultEng.text)
            self.jaTrans.append(resultJa.text)


    # 초기화
    def transReset(self):
        self.korEdit.clear()
        self.engTrans.clear()
        self.jaTrans.clear()




# 해상도별 글자크기 강제 고정하는 함수
def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"



# 해상도 고정
suppress_qt_warnings()
mp.freeze_support()



app = QApplication(sys.argv)



googlewin = GoogleTransApp()
googlewin.show()
sys.exit(app.exec_())