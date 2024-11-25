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



app = QApplication(sys.argv)

googlewin = GoogleTransApp()
googlewin.show()
sys.exit(app.exec_())