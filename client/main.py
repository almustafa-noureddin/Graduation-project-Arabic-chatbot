import sys 
import datetime 
import PyQt5 
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox 
from PyQt5.QtGui import QFont, QColor 
from PyQt5.QtGui import QIcon, QPixmap 
from network_interface import * 
from skin import * 
class Client(QDialog): 
    def __init__(self): 
        super().__init__() 
        self.ui = Ui_Dialog() 
        self.ui.setupUi(self) 
        self.setFixedSize(self.size()) 
        self.date = None 
        pixmap = QPixmap('avatar.png') 
        self.ui.labelAvatar.setPixmap(pixmap) 
        self.plain_font = QFont('Times New Roman', pointSize=11) 
        self.bold_font = QFont('Times New Roman', pointSize=11) 
        self.bold_font.setBold(True) 
        self.ui.textEditChat.setEnabled(False) 
        self.ui.pushButtonSend.clicked.connect(self.send) 
        self.setFixedSize(self.size()) 
        connect() 
    def send(self): 
        user_question = self.ui.lineEditAsk.text() 
        condition = user_question == '' or user_question.isspace() or len(user_question) < 3 
        if condition : 
            return self.ui.lineEditAsk.clear() 
        dt = datetime.datetime.now() 
        date = dt.date() 
        date_str = date.strftime('[ %d-%m-%y ]') 
        time_str = dt.time().strftime('%H:%M')
        self.ui.textEditChat.setCurrentFont(self.plain_font) 
        if self.date != date: 
            self.date = date 
            date_str = self.date.strftime('[ %d-%m-%y ]') 
            self.ui.textEditChat.append(date_str) 
            self.ui.textEditChat.setAlignment(PyQt5.QtCore.Qt.AlignCenter) 
        send(user_question) 
        responce = recv() 
        self.ui.textEditChat.append(time_str) 
        self.ui.textEditChat.append('') 
        self.ui.textEditChat.setAlignment(PyQt5.QtCore.Qt.AlignRight) 
        self.ui.textEditChat.setCurrentFont(self.bold_font) 
        self.ui.textEditChat.append(' أنت : '+user_question) 
        self.ui.textEditChat.setAlignment(PyQt5.QtCore.Qt.AlignRight) 
        self.ui.textEditChat.setCurrentFont(self.plain_font) 
        self.ui.textEditChat.setTextColor(QColor(255, 0, 0)) 
        self.ui.textEditChat.append(time_str) 
        self.ui.textEditChat.setAlignment(PyQt5.QtCore.Qt.AlignLeft) 
        self.ui.textEditChat.setCurrentFont(self.bold_font) 
        self.ui.textEditChat.append(' لينه : '+responce) 
        self.ui.textEditChat.setAlignment(PyQt5.QtCore.Qt.AlignLeft) 
        self.ui.textEditChat.setTextColor(QColor(0, 0, 0)) 
        self.ui.textEditChat.setEnabled(False) 
        return 
if __name__=="__main__": 
    app = QApplication(sys.argv) 
    w = Client()
    w.show() 
    sys.exit(app.exec_())