# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(399, 426)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 13, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 55, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 143, 91, 25))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 105, 171, 25))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(10, 260, 61, 25))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.sort = QtWidgets.QLineEdit(Form)
        self.sort.setGeometry(QtCore.QRect(70, 20, 241, 20))
        self.sort.setObjectName("sort")
        self.roasting = QtWidgets.QComboBox(Form)
        self.roasting.setGeometry(QtCore.QRect(190, 60, 161, 22))
        self.roasting.setObjectName("roasting")
        self.roasting.addItem("")
        self.roasting.addItem("")
        self.type = QtWidgets.QComboBox(Form)
        self.type.setGeometry(QtCore.QRect(190, 110, 121, 22))
        self.type.setObjectName("type")
        self.type.addItem("")
        self.type.addItem("")
        self.type.addItem("")
        self.description = QtWidgets.QPlainTextEdit(Form)
        self.description.setGeometry(QtCore.QRect(110, 150, 281, 101))
        self.description.setObjectName("description")
        self.price = QtWidgets.QLineEdit(Form)
        self.price.setGeometry(QtCore.QRect(80, 264, 113, 20))
        self.price.setObjectName("price")
        self.V_V = QtWidgets.QLineEdit(Form)
        self.V_V.setGeometry(QtCore.QRect(170, 305, 121, 20))
        self.V_V.setObjectName("V_V")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(10, 300, 151, 25))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.save_button = QtWidgets.QPushButton(Form)
        self.save_button.setGeometry(QtCore.QRect(244, 372, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.save_button.setFont(font)
        self.save_button.setObjectName("save_button")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "сорт"))
        self.label_2.setText(_translate("Form", "молотый/зерновой"))
        self.label_3.setText(_translate("Form", "Описание"))
        self.label_4.setText(_translate("Form", "степень прожарки"))
        self.label_5.setText(_translate("Form", "Цена"))
        self.roasting.setItemText(0, _translate("Form", "молотый"))
        self.roasting.setItemText(1, _translate("Form", "зерновой"))
        self.type.setItemText(0, _translate("Form", "легкая"))
        self.type.setItemText(1, _translate("Form", "средняя"))
        self.type.setItemText(2, _translate("Form", "сильная"))
        self.label_6.setText(_translate("Form", "Объем упаковки"))
        self.save_button.setText(_translate("Form", "Сохранить"))
