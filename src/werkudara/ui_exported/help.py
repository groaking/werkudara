# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './src/werkudara/ui/help.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName("About")
        About.resize(684, 506)
        self.buttonBox = QtWidgets.QDialogButtonBox(About)
        self.buttonBox.setGeometry(QtCore.QRect(590, 10, 81, 241))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.scrollArea = QtWidgets.QScrollArea(About)
        self.scrollArea.setGeometry(QtCore.QRect(10, 60, 471, 431))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 469, 429))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_message = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_message.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_message.setWordWrap(True)
        self.label_message.setObjectName("label_message")
        self.verticalLayout.addWidget(self.label_message)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label = QtWidgets.QLabel(About)
        self.label.setGeometry(QtCore.QRect(10, 10, 551, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(About)
        self.buttonBox.accepted.connect(About.accept) # type: ignore
        self.buttonBox.rejected.connect(About.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        _translate = QtCore.QCoreApplication.translate
        About.setWindowTitle(_translate("About", "Werkudara - HELP"))
        self.label_message.setText(_translate("About", "<html><head/><body><p>Visit <a href=\"https://github.com/groaking/werkudara\"><span style=\" text-decoration: underline; color:#0986d3;\">the official GitHub page of </span></a><a href=\"https://github.com/groaking/werkudara\"><span style=\" font-weight:600; text-decoration: underline; color:#0986d3;\">Werkudara</span></a> to read <span style=\" font-weight:600;\">Werkudara\'s</span> user manual and troubleshooting help.</p></body></html>"))
        self.label.setText(_translate("About", "Werkudara: How to use & Troubleshooting"))
