# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(530, 505)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.runButton = QtWidgets.QPushButton(self.centralWidget)
        self.runButton.setObjectName("runButton")
        self.horizontalLayout.addWidget(self.runButton)
        self.checkLimitation = QtWidgets.QCheckBox(self.centralWidget)
        self.checkLimitation.setChecked(True)
        self.checkLimitation.setObjectName("checkLimitation")
        self.horizontalLayout.addWidget(self.checkLimitation)
        self.limitationLineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.limitationLineEdit.setObjectName("limitationLineEdit")
        self.horizontalLayout.addWidget(self.limitationLineEdit)
        self.stepButton = QtWidgets.QPushButton(self.centralWidget)
        self.stepButton.setObjectName("stepButton")
        self.horizontalLayout.addWidget(self.stepButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.codeTextEdit = QtWidgets.QTextEdit(self.centralWidget)
        self.codeTextEdit.setObjectName("codeTextEdit")
        self.verticalLayout.addWidget(self.codeTextEdit)
        self.resultTextEdit = QtWidgets.QTextEdit(self.centralWidget)
        self.resultTextEdit.setReadOnly(True)
        self.resultTextEdit.setObjectName("resultTextEdit")
        self.verticalLayout.addWidget(self.resultTextEdit)
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.checkLimitation.toggled['bool'].connect(self.limitationLineEdit.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "/// Interpreter"))
        self.runButton.setText(_translate("MainWindow", "Run"))
        self.checkLimitation.setText(_translate("MainWindow", "Limit substitutions to:"))
        self.limitationLineEdit.setText(_translate("MainWindow", "1000"))
        self.stepButton.setText(_translate("MainWindow", "Step"))

