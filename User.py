<<<<<<< HEAD
# -*- coding: utf-8 -*-

from Reservation_Filehandling import Reservation_fileHandling
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow
from PyQt5.uic import loadUi
from Reservation import Reservation

class User(QMainWindow):
    def __init__(self, email):
        self.email = email
        super(User, self).__init__()
        loadUi('User.ui',self)        
        self.loginMsg = QMessageBox()
        self.setWindowTitle('Room Reservation')
        
        #Initialize Reservation Filhandling
        self.rfh = Reservation_fileHandling() 
        self.rfh.LoadDatabase() 
        #Set the text of lineEdit to organization using email 
        self.lineEdit_Organization.setText(self.rfh.GetOrganization(self.email))

        #Button Events
        self.pushButton_Reserve.clicked.connect(lambda: self.Reserve_Clicked())
            
    def Reserve_Clicked(self):
        self.newReservation = Reservation()
        self.ReservationInfo()
        
        self.newReservation.KeepReservation()
        print("CLICKED")
     
    def ReservationInfo(self):
        self.newReservation.SetNatureOfActivity(self.comboBox_NatureOfActivity.currentText())
        self.newReservation.SetOrganization(self.lineEdit_Organization.text())
        self.newReservation.SetRoom(self.comboBox_Room.currentText())
        #self.newReservation.SetMonth()
        #self.newReservation.SetDay()
        #self.newReservation.SetYear()
        self.newReservation.SetTimeIn(self.comboBox_timeStart.currentText())
        self.newReservation.SetTimeOut(self.comboBox_timeEnd.currentText())
"""       
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    widget = User("acsabesamis@mymail.mapua.edu.ph") #Still Testing
    widget.show()
    sys.exit(app.exec_())
"""
=======
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost! 

from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow
from PyQt5 import QtCore
from PyQt5.uic import loadUi

class User(QMainWindow):
    def __init__(self):
        super(User, self).__init__()
        loadUi('User.ui',self)
        self.loginMsg = QMessageBox()
        self.setWindowTitle('Room Reservation')
        
        #When Date is Selected
        self.calendarWidget.clicked.connect(self.showDate)
        
    def showDate(self):
        print(self.calendarWidget.selectedDate().toString(QtCore.Qt.ISODate))
        print(self.calendarWidget.lon
    def reserve_Clicked(self):
        print("value")
        
   
    
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    widget = User()
    widget.show()
    sys.exit(app.exec_())

>>>>>>> FRADEJAS
