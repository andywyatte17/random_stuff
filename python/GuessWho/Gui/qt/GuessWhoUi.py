# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GuessWho.ui'
#
# Created: Tue Sep  9 22:05:53 2014
#      by: PyQt4 UI code generator 4.10.4
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(758, 580)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(12, 6, 735, 518))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.verticalLayoutWidget)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.cb_08 = QtGui.QCheckBox(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_08.sizePolicy().hasHeightForWidth())
        self.cb_08.setSizePolicy(sizePolicy)
        self.cb_08.setMinimumSize(QtCore.QSize(70, 70))
        self.cb_08.setMaximumSize(QtCore.QSize(70, 70))
        self.cb_08.setObjectName(_fromUtf8("cb_08"))
        self.gridLayout.addWidget(self.cb_08, 1, 1, 1, 1)
        self.cb_20 = QtGui.QCheckBox(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_20.sizePolicy().hasHeightForWidth())
        self.cb_20.setSizePolicy(sizePolicy)
        self.cb_20.setMinimumSize(QtCore.QSize(70, 70))
        self.cb_20.setMaximumSize(QtCore.QSize(70, 70))
        self.cb_20.setObjectName(_fromUtf8("cb_20"))
        self.gridLayout.addWidget(self.cb_20, 3, 1, 1, 1)
        self.cb_21 = QtGui.QCheckBox(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_21.sizePolicy().hasHeightForWidth())
        self.cb_21.setSizePolicy(sizePolicy)
        self.cb_21.setMinimumSize(QtCore.QSize(70, 70))
        self.cb_21.setMaximumSize(QtCore.QSize(70, 70))
        self.cb_21.setObjectName(_fromUtf8("cb_21"))
        self.gridLayout.addWidget(self.cb_21, 3, 2, 1, 1)
        self.cb_17 = QtGui.QCheckBox(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_17.sizePolicy().hasHeightForWidth())
        self.cb_17.setSizePolicy(sizePolicy)
        self.cb_17.setMinimumSize(QtCore.QSize(70, 70))
        self.cb_17.setMaximumSize(QtCore.QSize(70, 70))
        self.cb_17.setObjectName(_fromUtf8("cb_17"))
        self.gridLayout.addWidget(self.cb_17, 2, 4, 1, 1)
        self.cb_10 = QtGui.QCheckBox(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_10.sizePolicy().hasHeightForWidth())
        self.cb_10.setSizePolicy(sizePolicy)
        self.cb_10.setMinimumSize(QtCore.QSize(70, 70))
        self.cb_10.setMaximumSize(QtCore.QSize(70, 70))
        self.cb_10.setObjectName(_fromUtf8("cb_10"))
        self.gridLayout.addWidget(self.cb_10, 1, 3, 1, 1)
        self.cb_24 = QtGui.QCheckBox(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_24.sizePolicy().hasHeightForWidth())
        self.cb_24.setSizePolicy(sizePolicy)
        self.cb_24.setMinimumSize(QtCore.QSize(70, 70))
        self.cb_24.setMaximumSize(QtCore.QSize(70, 70))
        self.cb_24.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cb_24.setObjectName(_fromUtf8("cb_24"))
        self.gridLayout.addWidget(self.cb_24, 3, 5, 1, 1)
        self.cb_22 = QtGui.QCheckBox(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_22.sizePolicy().hasHeightForWidth())
        self.cb_22.setSizePolicy(sizePolicy)
        self.cb_22.setMinimumSize(QtCore.QSize(70, 70))
        self.cb_22.setMaximumSize(QtCore.QSize(70, 70))
        self.cb_22.setObjectName(_fromUtf8("cb_22"))
        self.gridLayout.addWidget(self.cb_22, 3, 3, 1, 1)
        self.cb_07 = QtGui.QCheckBox(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_07.sizePolicy().hasHeightForWidth())
        self.cb_07.setSizePolicy(sizePolicy)
        self.cb_07.setMinimumSize(QtCore.QSize(70, 70))
        self.cb_07.setMaximumSize(QtCore.QSize(70, 70))
        self.cb_07.setObjectName(_fromUtf8("cb_07"))
        self.gridLayout.addWidget(self.cb_07, 1, 0, 1, 1)
        self.cb_16 = QtGui.QCheckBox(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_16.sizePolicy().hasHeightForWidth())
        self.cb_16.setSizePolicy(sizePolicy)
        self.cb_16.setMinimumSize(QtCore.QSize(70, 70))
        self.cb_16.setMaximumSize(QtCore.QSize(70, 70))
        self.cb_16.setObjectName(_fromUtf8("cb_16"))
        self.gridLayout.addWidget(self.cb_16, 2, 3, 1, 1)
        self.cb_09 = QtGui.QCheckBox(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_09.sizePolicy().hasHeightForWidth())
        self.cb_09.setSizePolicy(sizePolicy)
        self.cb_09.setMinimumSize(QtCore.QSize(70, 70))
        self.cb_09.setMaximumSize(QtCore.QSize(70, 70))
        self.cb_09.setObjectName(_fromUtf8("cb_09"))
        self.gridLayout.addWidget(self.cb_09, 1, 2, 1, 1)
        self.cb_03 = QtGui.QCheckBox(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_03.sizePolicy().hasHeightForWidth())
        self.cb_03.setSizePolicy(sizePolicy)
        self.cb_03.setMinimumSize(QtCore.QSize(70, 70))
        self.cb_03.setMaximumSize(QtCore.QSize(70, 70))
        self.cb_03.setObjectName(_fromUtf8("cb_03"))
        self.gridLayout.addWidget(self.cb_03, 0, 2, 1, 1)
        self.cb_14 = QtGui.QCheckBox(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_14.sizePolicy().hasHeightForWidth())
        self.cb_14.setSizePolicy(sizePolicy)
        self.cb_14.setMinimumSize(QtCore.QSize(70, 70))
        self.cb_14.setMaximumSize(QtCore.QSize(70, 70))
        self.cb_14.setObjectName(_fromUtf8("cb_14"))
        self.gridLayout.addWidget(self.cb_14, 2, 2, 1, 1)
        self.cb_23 = QtGui.QCheckBox(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_23.sizePolicy().hasHeightForWidth())
        self.cb_23.setSizePolicy(sizePolicy)
        self.cb_23.setMinimumSize(QtCore.QSize(70, 70))
        self.cb_23.setMaximumSize(QtCore.QSize(70, 70))
        self.cb_23.setObjectName(_fromUtf8("cb_23"))
        self.gridLayout.addWidget(self.cb_23, 3, 4, 1, 1)
        self.cb_15 = QtGui.QCheckBox(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_15.sizePolicy().hasHeightForWidth())
        self.cb_15.setSizePolicy(sizePolicy)
        self.cb_15.setMinimumSize(QtCore.QSize(70, 70))
        self.cb_15.setMaximumSize(QtCore.QSize(70, 70))
        self.cb_15.setObjectName(_fromUtf8("cb_15"))
        self.gridLayout.addWidget(self.cb_15, 2, 1, 1, 1)
        self.cb_02 = QtGui.QCheckBox(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_02.sizePolicy().hasHeightForWidth())
        self.cb_02.setSizePolicy(sizePolicy)
        self.cb_02.setMinimumSize(QtCore.QSize(70, 70))
        self.cb_02.setMaximumSize(QtCore.QSize(70, 70))
        self.cb_02.setObjectName(_fromUtf8("cb_02"))
        self.gridLayout.addWidget(self.cb_02, 0, 1, 1, 1)
        self.cb_04 = QtGui.QCheckBox(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_04.sizePolicy().hasHeightForWidth())
        self.cb_04.setSizePolicy(sizePolicy)
        self.cb_04.setMinimumSize(QtCore.QSize(70, 70))
        self.cb_04.setMaximumSize(QtCore.QSize(70, 70))
        self.cb_04.setObjectName(_fromUtf8("cb_04"))
        self.gridLayout.addWidget(self.cb_04, 0, 3, 1, 1)
        self.cb_01 = QtGui.QCheckBox(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_01.sizePolicy().hasHeightForWidth())
        self.cb_01.setSizePolicy(sizePolicy)
        self.cb_01.setMinimumSize(QtCore.QSize(70, 70))
        self.cb_01.setMaximumSize(QtCore.QSize(70, 70))
        self.cb_01.setObjectName(_fromUtf8("cb_01"))
        self.gridLayout.addWidget(self.cb_01, 0, 0, 1, 1)
        self.cb_11 = QtGui.QCheckBox(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_11.sizePolicy().hasHeightForWidth())
        self.cb_11.setSizePolicy(sizePolicy)
        self.cb_11.setMinimumSize(QtCore.QSize(70, 70))
        self.cb_11.setMaximumSize(QtCore.QSize(70, 70))
        self.cb_11.setObjectName(_fromUtf8("cb_11"))
        self.gridLayout.addWidget(self.cb_11, 1, 4, 1, 1)
        self.cb_18 = QtGui.QCheckBox(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_18.sizePolicy().hasHeightForWidth())
        self.cb_18.setSizePolicy(sizePolicy)
        self.cb_18.setMinimumSize(QtCore.QSize(70, 70))
        self.cb_18.setMaximumSize(QtCore.QSize(70, 70))
        self.cb_18.setObjectName(_fromUtf8("cb_18"))
        self.gridLayout.addWidget(self.cb_18, 2, 5, 1, 1)
        self.cb_12 = QtGui.QCheckBox(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_12.sizePolicy().hasHeightForWidth())
        self.cb_12.setSizePolicy(sizePolicy)
        self.cb_12.setMinimumSize(QtCore.QSize(70, 70))
        self.cb_12.setMaximumSize(QtCore.QSize(70, 70))
        self.cb_12.setObjectName(_fromUtf8("cb_12"))
        self.gridLayout.addWidget(self.cb_12, 1, 5, 1, 1)
        self.cb_05 = QtGui.QCheckBox(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_05.sizePolicy().hasHeightForWidth())
        self.cb_05.setSizePolicy(sizePolicy)
        self.cb_05.setMinimumSize(QtCore.QSize(70, 70))
        self.cb_05.setMaximumSize(QtCore.QSize(70, 70))
        self.cb_05.setObjectName(_fromUtf8("cb_05"))
        self.gridLayout.addWidget(self.cb_05, 0, 4, 1, 1)
        self.cb_06 = QtGui.QCheckBox(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_06.sizePolicy().hasHeightForWidth())
        self.cb_06.setSizePolicy(sizePolicy)
        self.cb_06.setMinimumSize(QtCore.QSize(70, 70))
        self.cb_06.setMaximumSize(QtCore.QSize(70, 70))
        self.cb_06.setObjectName(_fromUtf8("cb_06"))
        self.gridLayout.addWidget(self.cb_06, 0, 5, 1, 1)
        self.cb_13 = QtGui.QCheckBox(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_13.sizePolicy().hasHeightForWidth())
        self.cb_13.setSizePolicy(sizePolicy)
        self.cb_13.setMinimumSize(QtCore.QSize(70, 70))
        self.cb_13.setMaximumSize(QtCore.QSize(70, 70))
        self.cb_13.setObjectName(_fromUtf8("cb_13"))
        self.gridLayout.addWidget(self.cb_13, 2, 0, 1, 1)
        self.cb_19 = QtGui.QCheckBox(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_19.sizePolicy().hasHeightForWidth())
        self.cb_19.setSizePolicy(sizePolicy)
        self.cb_19.setMinimumSize(QtCore.QSize(70, 70))
        self.cb_19.setMaximumSize(QtCore.QSize(70, 70))
        self.cb_19.setObjectName(_fromUtf8("cb_19"))
        self.gridLayout.addWidget(self.cb_19, 3, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lv_questions = QtGui.QListView(self.verticalLayoutWidget)
        self.lv_questions.setObjectName(_fromUtf8("lv_questions"))
        self.horizontalLayout.addWidget(self.lv_questions)
        self.cb_person = QtGui.QCheckBox(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_person.sizePolicy().hasHeightForWidth())
        self.cb_person.setSizePolicy(sizePolicy)
        self.cb_person.setMinimumSize(QtCore.QSize(100, 100))
        self.cb_person.setMaximumSize(QtCore.QSize(100, 100))
        self.cb_person.setObjectName(_fromUtf8("cb_person"))
        self.horizontalLayout.addWidget(self.cb_person)
        self.btn_ask = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btn_ask.setObjectName(_fromUtf8("btn_ask"))
        self.horizontalLayout.addWidget(self.btn_ask)
        self.lv_answers = QtGui.QListView(self.verticalLayoutWidget)
        self.lv_answers.setObjectName(_fromUtf8("lv_answers"))
        self.horizontalLayout.addWidget(self.lv_answers)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 758, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.cb_08.setText(_translate("MainWindow", "CheckBox", None))
        self.cb_20.setText(_translate("MainWindow", "CheckBox", None))
        self.cb_21.setText(_translate("MainWindow", "CheckBox", None))
        self.cb_17.setText(_translate("MainWindow", "CheckBox", None))
        self.cb_10.setText(_translate("MainWindow", "CheckBox", None))
        self.cb_24.setText(_translate("MainWindow", "CheckBox", None))
        self.cb_22.setText(_translate("MainWindow", "CheckBox", None))
        self.cb_07.setText(_translate("MainWindow", "CheckBox", None))
        self.cb_16.setText(_translate("MainWindow", "CheckBox", None))
        self.cb_09.setText(_translate("MainWindow", "CheckBox", None))
        self.cb_03.setText(_translate("MainWindow", "CheckBox", None))
        self.cb_14.setText(_translate("MainWindow", "CheckBox", None))
        self.cb_23.setText(_translate("MainWindow", "CheckBox", None))
        self.cb_15.setText(_translate("MainWindow", "CheckBox", None))
        self.cb_02.setText(_translate("MainWindow", "CheckBox", None))
        self.cb_04.setText(_translate("MainWindow", "CheckBox", None))
        self.cb_01.setText(_translate("MainWindow", "CheckBox", None))
        self.cb_11.setText(_translate("MainWindow", "CheckBox", None))
        self.cb_18.setText(_translate("MainWindow", "CheckBox", None))
        self.cb_12.setText(_translate("MainWindow", "CheckBox", None))
        self.cb_05.setText(_translate("MainWindow", "CheckBox", None))
        self.cb_06.setText(_translate("MainWindow", "CheckBox", None))
        self.cb_13.setText(_translate("MainWindow", "CheckBox", None))
        self.cb_19.setText(_translate("MainWindow", "CheckBox", None))
        self.cb_person.setText(_translate("MainWindow", "CheckBox", None))
        self.btn_ask.setText(_translate("MainWindow", "PushButton", None))

