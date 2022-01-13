# -*- coding: utf-8 -*- # Form implementation generated from reading ui file 'skin.ui' 
# # # Created by: PyQt5 UI code generator 5.14.2 
# # # WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets 
class Ui_Dialog(object): 
    def setupUi(self, Dialog): 
        Dialog.setObjectName("Dialog") 
        Dialog.resize(1069, 524) 
        Dialog.setSizeGripEnabled(False) 
        self.labelAvatar = QtWidgets.QLabel(Dialog) 
        self.labelAvatar.setGeometry(QtCore.QRect(20, 20, 300, 486)) 
        self.labelAvatar.setText("") 
        self.labelAvatar.setObjectName("labelAvatar") 
        self.widget = QtWidgets.QWidget(Dialog) 
        self.widget.setGeometry(QtCore.QRect(330, 20, 731, 491)) 
        self.widget.setObjectName("widget") 
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget) 
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout") 
        self.textEditChat = QtWidgets.QTextEdit(self.widget) 
        self.textEditChat.setReadOnly(True) 
        self.textEditChat.setObjectName("textEditChat") 
        self.verticalLayout.addWidget(self.textEditChat) 
        self.horizontalLayout = QtWidgets.QHBoxLayout() 
        self.horizontalLayout.setObjectName("horizontalLayout") 
        self.pushButtonSend = QtWidgets.QPushButton(self.widget) 
        font = QtGui.QFont() 
        font.setFamily("Times New Roman") 
        font.setPointSize(10) 
        font.setBold(True) 
        font.setWeight(75) 
        self.pushButtonSend.setFont(font) 
        self.pushButtonSend.setObjectName("pushButtonSend") 
        self.horizontalLayout.addWidget(self.pushButtonSend) 
        self.lineEditAsk = QtWidgets.QLineEdit(self.widget) 
        self.lineEditAsk.setObjectName("lineEditAsk") 
        self.horizontalLayout.addWidget(self.lineEditAsk) 
        self.verticalLayout.addLayout(self.horizontalLayout) 
        self.retranslateUi(Dialog) 
        QtCore.QMetaObject.connectSlotsByName(Dialog) 
    def retranslateUi(self, Dialog): 
        _translate = QtCore.QCoreApplication.translate 
        Dialog.setWindowTitle(_translate("Dialog", "Lina Chatbot"))
        self.textEditChat.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n" "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n" "p, li { white-space: pre-wrap; }\n" "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n" "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButtonSend.setText(_translate("Dialog", "إرسال "))
if __name__ == "__main__": pass