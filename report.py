# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'report.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox


class Ui_Form(object):
    
    def generateReport(self):
      num1 = self.marks1.text() 
      num2 = self.marks2.text()
      num3 = self.marks3.text()
      num4 = self.marks4.text()
      num5 = self.marks5.text()

      a= []
      suppli = ""
      totalsuppli = 0
      total = 0
      gpa = 0
      a.append(int(num1))
      a.append(int(num2))
      a.append(int(num3))
      a.append(int(num4))
      a.append(int(num5))


      for i in range (len(a)) :
        if a[i] >=40 :
          total = total+a[i]
        else :
          suppli+=" " +("Subject"+" "+str(i+1))+", "
          totalsuppli+=1


      gpa = total /(5-totalsuppli)

      print (gpa)
      print (suppli)

      msg = QMessageBox()
      # msg.setIcon(QMessageBox.Critical)
      msg.setText("Percentage is : "+str(gpa)+"\n"+"Total Supplies : "+str(totalsuppli)+"\n"+ "Failed in Subjects : "+ str(suppli))
      msg.setWindowTitle("Answer")
      msg.exec()






    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(372, 601)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(70, 100, 54, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(70, 160, 54, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(70, 220, 54, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(70, 280, 54, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(70, 340, 54, 17))
        self.label_5.setObjectName("label_5")
        self.marks1 = QtWidgets.QLineEdit(Form)
        self.marks1.setGeometry(QtCore.QRect(170, 90, 113, 25))
        self.marks1.setObjectName("marks1")
        self.marks2 = QtWidgets.QLineEdit(Form)
        self.marks2.setGeometry(QtCore.QRect(170, 150, 113, 25))
        self.marks2.setObjectName("marks2")
        self.marks3 = QtWidgets.QLineEdit(Form)
        self.marks3.setGeometry(QtCore.QRect(170, 220, 113, 25))
        self.marks3.setObjectName("marks3")
        self.marks4 = QtWidgets.QLineEdit(Form)
        self.marks4.setGeometry(QtCore.QRect(170, 280, 113, 25))
        self.marks4.setObjectName("marks4")
        self.marks5 = QtWidgets.QLineEdit(Form)
        self.marks5.setGeometry(QtCore.QRect(170, 340, 113, 25))
        self.marks5.setObjectName("marks5")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(120, 450, 101, 61))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.generateReport)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Subject 1"))
        self.label_2.setText(_translate("Form", "Subject 2"))
        self.label_3.setText(_translate("Form", "Subject 3"))
        self.label_4.setText(_translate("Form", "Subject 4"))
        self.label_5.setText(_translate("Form", "Subject 5"))
        self.pushButton.setText(_translate("Form", "Generate Report"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Form()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

