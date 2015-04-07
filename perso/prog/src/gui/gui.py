# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\gtheurillat\workspace_jouve\CutImg_1in2\perso\prog\src\gui\cut_images.ui'
#
# Created: Fri May 09 17:37:17 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_GroupBox(object):
    def setupUi(self, GroupBox):
        GroupBox.setObjectName(_fromUtf8("GroupBox"))
        GroupBox.resize(804, 510)
        self.verticalLayoutWidget = QtGui.QWidget(GroupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 19, 790, 481))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.inputText = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.inputText.setObjectName(_fromUtf8("inputText"))
        self.horizontalLayout.addWidget(self.inputText)
        self.inputButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.inputButton.setObjectName(_fromUtf8("inputButton"))
        self.horizontalLayout.addWidget(self.inputButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.outputText = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.outputText.setObjectName(_fromUtf8("outputText"))
        self.horizontalLayout_8.addWidget(self.outputText)
        self.outputButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.outputButton.setObjectName(_fromUtf8("outputButton"))
        self.horizontalLayout_8.addWidget(self.outputButton)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.radioGD = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.radioGD.setObjectName(_fromUtf8("radioGD"))
        self.horizontalLayout_10.addWidget(self.radioGD)
        self.radioDG = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.radioDG.setObjectName(_fromUtf8("radioDG"))
        self.horizontalLayout_10.addWidget(self.radioDG)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.runButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.runButton.setObjectName(_fromUtf8("runButton"))
        self.verticalLayout.addWidget(self.runButton)
        self.progressBar = QtGui.QProgressBar(self.verticalLayoutWidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout.addWidget(self.progressBar)
        self.logText = QtGui.QPlainTextEdit(self.verticalLayoutWidget)
        self.logText.setObjectName(_fromUtf8("logText"))
        self.verticalLayout.addWidget(self.logText)

        self.retranslateUi(GroupBox)
        QtCore.QMetaObject.connectSlotsByName(GroupBox)

    def retranslateUi(self, GroupBox):
        GroupBox.setWindowTitle(_translate("GroupBox", "GroupBox", None))
        GroupBox.setTitle(_translate("GroupBox", "Cut Images 2 in 1 (v1.0)", None))
        self.inputButton.setText(_translate("GroupBox", "Input Folder", None))
        self.outputButton.setText(_translate("GroupBox", "Output Folder", None))
        self.radioGD.setText(_translate("GroupBox", "Lecture de Gauche à droite", None))
        self.radioDG.setText(_translate("GroupBox", "Lecture de droite à gauche", None))
        self.runButton.setText(_translate("GroupBox", "C\'est partie!", None))

