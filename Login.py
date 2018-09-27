# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from Reservation_User import Ui_MainWindow
from Reservation_Admin import Ui_MainWindowAdmin
import signUp
import Login_Filehandling

class Ui_login_Form(object):
    
    def Login_Clicked(self, login_Form):
        
        if self.lfh.LoadDatabase() is True:
            if self.lineEdit_userName.text() == '' or self.lineEdit_password.text() == '':
                self.label_state.setText("Please complete all fields!")
            else:
                if self.lfh.GetPasswordByEmail(self.lineEdit_userName.text()) == -1:
                  self.label_state.setText("Invalid Credentials")
                  self.lineEdit_userName.clear()
                  self.lineEdit_password.clear()
                else:
                    if self.lineEdit_password.text() != self.lfh.GetPasswordByEmail(self.lineEdit_userName.text()):
                        self.label_state.setText("Incorrect Password!")
                        self.lineEdit_password.clear()
                    else:
                        self.label_state.clear()
                        self.loginMsg.setText('Login Successful!')
                        self.loginMsg.exec_()
                        if self.lfh.AccountType(self.lineEdit_userName.text())=="Admin":
                            window = QtWidgets.QMainWindow()
                            ui = Ui_MainWindowAdmin()
                            ui.setup(window)
                            window.show()
                        else:
                            window = QtWidgets.QMainWindow()
                            ui = Ui_MainWindow()
                            ui.setup(window)
                            window.show()
                        self.lineEdit_userName.clear()
                        self.lineEdit_password.clear()
        else:
            print("Program Exits")         
            
        #Close Database
        self.lfh.CloseDatabase()
                     
    def Signup_Clicked(self, login_Form):
        #Opens SignUp Dialog    
        window = QtWidgets.QMainWindow()
        ui = Ui_MainWindowAdmin()
        ui.setup(window)
        window.show()
        #signUpWindow = signUp.signUp()
        #signUpWindow.exec_()
        
        
    def setupUi(self, login_Form):
        #######################################################################
        self.lfh = Login_Filehandling.Login_fileHandling()
        self.loginMsg = QMessageBox()
        self.loginMsg.setWindowTitle('Reservation')   
        #######################################################################
        login_Form.setObjectName("login_Form")
        login_Form.resize(487, 374)
        self.lineEdit_userName = QtWidgets.QLineEdit(login_Form)
        self.lineEdit_userName.setGeometry(QtCore.QRect(120, 110, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.lineEdit_userName.setFont(font)
        self.lineEdit_userName.setObjectName("lineEdit_userName")
        self.lineEdit_password = QtWidgets.QLineEdit(login_Form)
        self.lineEdit_password.setGeometry(QtCore.QRect(120, 160, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.lineEdit_password.setFont(font)
        self.lineEdit_password.setText("")
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pushButton_login = QtWidgets.QPushButton(login_Form)
        self.pushButton_login.setGeometry(QtCore.QRect(210, 210, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.pushButton_login.setFont(font)
        self.pushButton_login.setObjectName("pushButton_login")
        ###############################################################################
        self.pushButton_login.clicked.connect(lambda: self.Login_Clicked(login_Form))
        ################################################################################
        self.createAccount_commandLinkButton = QtWidgets.QCommandLinkButton(login_Form)
        self.createAccount_commandLinkButton.setGeometry(QtCore.QRect(310, 320, 171, 48))
        self.createAccount_commandLinkButton.setObjectName("createAccount_commandLinkButton")
        self.label_userName = QtWidgets.QLabel(login_Form)
        self.label_userName.setGeometry(QtCore.QRect(20, 110, 101, 31))
        ####################################################################################
        self.createAccount_commandLinkButton.clicked.connect(lambda: self.Signup_Clicked(login_Form))
        #####################################################################################
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_userName.setFont(font)
        self.label_userName.setObjectName("label_userName")
        self.label_password = QtWidgets.QLabel(login_Form)
        self.label_password.setGeometry(QtCore.QRect(20, 160, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_password.setFont(font)
        self.label_password.setObjectName("label_password")
        self.label_state = QtWidgets.QLabel(login_Form)
        self.label_state.setGeometry(QtCore.QRect(140, 70, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_state.setFont(font)
        self.label_state.setText("")
        self.label_state.setObjectName("label_state")

        self.retranslateUi(login_Form)
        QtCore.QMetaObject.connectSlotsByName(login_Form)

    def retranslateUi(self, login_Form):
        _translate = QtCore.QCoreApplication.translate
        login_Form.setWindowTitle(_translate("login_Form", "Reservation"))
        self.pushButton_login.setText(_translate("login_Form", "Login"))
        self.createAccount_commandLinkButton.setText(_translate("login_Form", "Create Account"))
        self.label_userName.setText(_translate("login_Form", "Username"))
        self.label_password.setText(_translate("login_Form", "Password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login_Form = QtWidgets.QWidget()
    ui = Ui_login_Form()
    ui.setupUi(login_Form)
    login_Form.show()
    sys.exit(app.exec_())

