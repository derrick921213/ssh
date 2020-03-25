from PyQt5 import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel,QPushButton, QLineEdit, QMenuBar, QStatusBar
import paramiko as s
import sys,ping,os
from paramiko import SSHException
#----------------------------------------------------------------#
#class MainWindow(QtWidgets.QMainWindow):
 #   def __init__(self):
  #      super(MainWindow,self).__init__()
   #     self.ui = Ui_Dialog()
    #    self.ui.setupUi(self)
     #   self.ui.pushButton_2.clicked.connect(self.exit)
      #  self.ui.pushButton.clicked.connect(self.buttonclicked)
       # ip = self.ui.lineEdit_4.text()
        #self.ui.pushButton_3.clicked.connect(self.ping)
    #def exit(self):
     #   sys.exit(app.exec_())
   # def buttonclicked(self):
    #    user = self.ui.lineEdit.text()
     #   pwd = self.ui.lineEdit_2.text()
      #  ip = self.ui.lineEdit_4.text()
       # ssh = s.SSHClient()
        #ssh.set_missing_host_key_policy(s.AutoAddPolicy())
        #if user or pwd or ip == None:
         #   e = ssh.connect(hostname=ip, username=user, password=pwd)
          #  ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('ls')
           # for i in ssh_stdout:
            #    self.ui.plainTextEdit.appendPlainText(i)
        #else:  
         #   self.ui.plainTextEdit.appendPlainText("connect error!!")

    #def ping (self):
     #   name = "127.0.0.1"
      #  response = os.system('ping -n 1 %s'%name)
       # if response == 0:
        #    self.ui.plainTextEdit.appendPlainText(name+" is up")
        #else:
         #   self.ui.plainTextEdit.appendPlainText(name+" is down!!")
#-------------------------------------------------------------------------#
class login(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(834, 464)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(210, 120, 151, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(210, 180, 151, 22))
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setReadOnly(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 330, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(20)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(70, 250, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 180, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(100, 330, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 120, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(210, 260, 151, 22))
        self.lineEdit_4.setInputMask("")
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_4.setReadOnly(False)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(50, 40, 361, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe 繁黑體 Std B")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(450, 20, 321, 421))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(140, 390, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "管理後臺"))
        self.pushButton_2.setText(_translate("Dialog", "關閉"))
        self.label_3.setText(_translate("Dialog", "Hostname:"))
        self.label_2.setText(_translate("Dialog", "password:"))
        self.pushButton.setText(_translate("Dialog", "登入"))
        self.label.setText(_translate("Dialog", "user:"))
        self.label_4.setText(_translate("Dialog", "歡迎登入星夜伺服器後台"))
        self.pushButton_3.setText(_translate("Dialog", "測試主機"))
#----------------------------------------------------------------------------------#
class after(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(928, 515)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(20, 330, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 380, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 430, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 480, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(30, 10, 861, 301))
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "PushButton"))
        self.pushButton_2.setText(_translate("Dialog", "PushButton"))
        self.pushButton_3.setText(_translate("Dialog", "PushButton"))
        self.pushButton_4.setText(_translate("Dialog", "PushButton"))
#--------------------------------------------------------------------------#
                        
if __name__== '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = login()
    ui.setupUi(MainWindow)

    
    sys.exit(app.exec_())            