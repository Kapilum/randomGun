# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\01.Code\01.bg_randomGun\randomGun\randomGunLayout.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

import random
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets

# 공통 총기
AR = ["M16A4", "M416", "AKM", "ㅡBEㅡ", "MK47"]
SMG = ["Vector", "Micro UZI", "UMP45"]
SR = ["Kar98K", "M24"]
DMR = ["SKS", "SLR"]
MISC = ["HanJo"]

# 맵 한정 총기
ErangelAR = ["SCAR-L", "PP-19 Bizon", "DP-28"]
ErangelDMR = ["VSS", "Mini-14"]
MiramarAR = ["SCAR-L"]
MiramarDMR = ["VSS", "Mini-14"]
MiramarSR = ["Win94"]
SanhokAR = ["QBZ"]
SanhokDMR = ["QBU", "VSS"]
KarakinAR = ["SCAR-L"]
KarakinDMR = ["Mini-14"]
KarakinSR = ["Win94"]

# SG + ㅡ그ㅡ 모드
ModSGT = ["S686", "S1897", "S12K", "Tommy Gun"]

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(560, 400)
        MainWindow.setMinimumSize(QtCore.QSize(560, 400))
        MainWindow.setMaximumSize(QtCore.QSize(560, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./img/dices.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.randomGun = QtWidgets.QWidget(MainWindow)
        self.randomGun.setMaximumSize(QtCore.QSize(560, 500))
        self.randomGun.setStyleSheet("background-color: rgba(255, 255, 255, 255);")
        self.randomGun.setObjectName("randomGun")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.randomGun)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 130, 561, 111))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(6, 0, 6, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.setMapE = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.setMapE.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.setMapE.sizePolicy().hasHeightForWidth())
        self.setMapE.setSizePolicy(sizePolicy)
        self.setMapE.setMaximumSize(QtCore.QSize(140, 140))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.setMapE.setFont(font)
        self.setMapE.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.setMapE.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./img/erangel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setMapE.setIcon(icon1)
        self.setMapE.setIconSize(QtCore.QSize(150, 170))
        self.setMapE.setCheckable(False)
        self.setMapE.setChecked(False)
        self.setMapE.setObjectName("setMapE")
        self.horizontalLayout.addWidget(self.setMapE)
        self.setMapM = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.setMapM.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.setMapM.sizePolicy().hasHeightForWidth())
        self.setMapM.setSizePolicy(sizePolicy)
        self.setMapM.setMaximumSize(QtCore.QSize(140, 140))
        self.setMapM.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.setMapM.setAutoFillBackground(False)
        self.setMapM.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./img/mirama.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setMapM.setIcon(icon2)
        self.setMapM.setIconSize(QtCore.QSize(180, 150))
        self.setMapM.setShortcut("")
        self.setMapM.setAutoRepeat(False)
        self.setMapM.setObjectName("setMapM")
        self.horizontalLayout.addWidget(self.setMapM)
        self.setMapS = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.setMapS.sizePolicy().hasHeightForWidth())
        self.setMapS.setSizePolicy(sizePolicy)
        self.setMapS.setMaximumSize(QtCore.QSize(140, 140))
        self.setMapS.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("./img/sanhok.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setMapS.setIcon(icon3)
        self.setMapS.setIconSize(QtCore.QSize(150, 150))
        self.setMapS.setObjectName("setMapS")
        self.horizontalLayout.addWidget(self.setMapS)
        self.setMapK = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.setMapK.sizePolicy().hasHeightForWidth())
        self.setMapK.setSizePolicy(sizePolicy)
        self.setMapK.setMaximumSize(QtCore.QSize(140, 140))
        self.setMapK.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("./img/karakin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setMapK.setIcon(icon4)
        self.setMapK.setIconSize(QtCore.QSize(200, 200))
        self.setMapK.setShortcut("")
        self.setMapK.setObjectName("setMapK")
        self.horizontalLayout.addWidget(self.setMapK)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.randomGun)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(280, 40, 91, 91))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.rollChk = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.rollChk.setContentsMargins(0, 0, 0, 0)
        self.rollChk.setObjectName("rollChk")
        self.setRoll1 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.setRoll1.setFont(font)
        self.setRoll1.setObjectName("setRoll1")
        self.rollChk.addWidget(self.setRoll1)
        self.setRoll2 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.setRoll2.setFont(font)
        self.setRoll2.setChecked(True)
        self.setRoll2.setObjectName("setRoll2")
        self.rollChk.addWidget(self.setRoll2)
        self.setRoll3 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.setRoll3.setFont(font)
        self.setRoll3.setObjectName("setRoll3")
        self.rollChk.addWidget(self.setRoll3)
        self.rerollChk = QtWidgets.QCheckBox(self.randomGun)
        self.rerollChk.setGeometry(QtCore.QRect(400, 70, 121, 31))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.rerollChk.setFont(font)
        self.rerollChk.setAutoFillBackground(False)
        self.rerollChk.setCheckable(True)
        self.rerollChk.setChecked(True)
        self.rerollChk.setObjectName("rerollChk")
        self.setPlayer = QtWidgets.QSpinBox(self.randomGun)
        self.setPlayer.setGeometry(QtCore.QRect(450, 50, 71, 20))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setBold(False)
        font.setWeight(50)
        self.setPlayer.setFont(font)
        self.setPlayer.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.setPlayer.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.setPlayer.setFrame(True)
        self.setPlayer.setSpecialValueText("")
        self.setPlayer.setMinimum(1)
        self.setPlayer.setMaximum(4)
        self.setPlayer.setProperty("value", 4)
        self.setPlayer.setObjectName("setPlayer")
        self.labelP = QtWidgets.QLabel(self.randomGun)
        self.labelP.setGeometry(QtCore.QRect(400, 49, 51, 20))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.labelP.setFont(font)
        self.labelP.setObjectName("labelP")
        self.labelRoll1 = QtWidgets.QLabel(self.randomGun)
        self.labelRoll1.setGeometry(QtCore.QRect(10, 50, 211, 16))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.labelRoll1.setFont(font)
        self.labelRoll1.setObjectName("labelRoll1")
        self.labelRoll2 = QtWidgets.QLabel(self.randomGun)
        self.labelRoll2.setGeometry(QtCore.QRect(10, 65, 241, 41))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.labelRoll2.setFont(font)
        self.labelRoll2.setObjectName("labelRoll2")
        self.labelRoll3 = QtWidgets.QLabel(self.randomGun)
        self.labelRoll3.setGeometry(QtCore.QRect(10, 100, 191, 21))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.labelRoll3.setFont(font)
        self.labelRoll3.setObjectName("labelRoll3")
        self.banner = QtWidgets.QLabel(self.randomGun)
        self.banner.setGeometry(QtCore.QRect(0, 0, 561, 41))
        self.banner.setText("")
        self.banner.setPixmap(QtGui.QPixmap("./img/banner1.png"))
        self.banner.setScaledContents(True)
        self.banner.setObjectName("banner")
        self.onSGT = QtWidgets.QCheckBox(self.randomGun)
        self.onSGT.setGeometry(QtCore.QRect(400, 100, 121, 21))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.onSGT.setFont(font)
        self.onSGT.setAutoFillBackground(False)
        self.onSGT.setCheckable(True)
        self.onSGT.setChecked(False)
        self.onSGT.setObjectName("onSGT")
        self.groupBox = QtWidgets.QGroupBox(self.randomGun)
        self.groupBox.setGeometry(QtCore.QRect(10, 250, 541, 141))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 30, 231, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.resultP1 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.resultP1.setContentsMargins(0, 0, 0, 0)
        self.resultP1.setObjectName("resultP1")
        self.Player1 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.Player1.setMinimumSize(QtCore.QSize(50, 0))
        self.Player1.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setBold(True)
        font.setWeight(75)
        self.Player1.setFont(font)
        self.Player1.setStyleSheet("background-color: rgba(255, 255, 0, 150);")
        self.Player1.setAlignment(QtCore.Qt.AlignCenter)
        self.Player1.setObjectName("Player1")
        self.resultP1.addWidget(self.Player1)
        self.slotP1 = QtWidgets.QListWidget(self.horizontalLayoutWidget_2)
        self.slotP1.setLineWidth(12)
        self.slotP1.setMidLineWidth(2)
        self.slotP1.setModelColumn(0)
        self.slotP1.setObjectName("slotP1")
        self.resultP1.addWidget(self.slotP1)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(30, 80, 231, 41))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.resultP2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.resultP2.setContentsMargins(0, 0, 0, 0)
        self.resultP2.setObjectName("resultP2")
        self.Player2 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.Player2.setMinimumSize(QtCore.QSize(50, 0))
        self.Player2.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setBold(True)
        font.setWeight(75)
        self.Player2.setFont(font)
        self.Player2.setStyleSheet("background-color: rgba(255, 79, 48,220);")
        self.Player2.setAlignment(QtCore.Qt.AlignCenter)
        self.Player2.setObjectName("Player2")
        self.resultP2.addWidget(self.Player2)
        self.slotP2 = QtWidgets.QListWidget(self.horizontalLayoutWidget_4)
        self.slotP2.setLineWidth(12)
        self.slotP2.setMidLineWidth(2)
        self.slotP2.setModelColumn(0)
        self.slotP2.setObjectName("slotP2")
        self.resultP2.addWidget(self.slotP2)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(290, 80, 231, 41))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.resultP4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.resultP4.setContentsMargins(0, 0, 0, 0)
        self.resultP4.setObjectName("resultP4")
        self.Player4 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.Player4.setMinimumSize(QtCore.QSize(50, 0))
        self.Player4.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setBold(True)
        font.setWeight(75)
        self.Player4.setFont(font)
        self.Player4.setStyleSheet("background-color: rgba(9, 163, 104,220);")
        self.Player4.setAlignment(QtCore.Qt.AlignCenter)
        self.Player4.setObjectName("Player4")
        self.resultP4.addWidget(self.Player4)
        self.slotP4 = QtWidgets.QListWidget(self.horizontalLayoutWidget_5)
        self.slotP4.setLineWidth(12)
        self.slotP4.setMidLineWidth(2)
        self.slotP4.setModelColumn(0)
        self.slotP4.setObjectName("slotP4")
        self.resultP4.addWidget(self.slotP4)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(290, 30, 231, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.resultP3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.resultP3.setContentsMargins(0, 0, 0, 0)
        self.resultP3.setObjectName("resultP3")
        self.Player3 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.Player3.setMinimumSize(QtCore.QSize(50, 0))
        self.Player3.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setBold(True)
        font.setWeight(75)
        self.Player3.setFont(font)
        self.Player3.setStyleSheet("background-color: rgb(28, 64, 218,220);")
        self.Player3.setAlignment(QtCore.Qt.AlignCenter)
        self.Player3.setObjectName("Player3")
        self.resultP3.addWidget(self.Player3)
        self.slotP3 = QtWidgets.QListWidget(self.horizontalLayoutWidget_3)
        self.slotP3.setLineWidth(12)
        self.slotP3.setMidLineWidth(2)
        self.slotP3.setModelColumn(0)
        self.slotP3.setObjectName("slotP3")
        self.resultP3.addWidget(self.slotP3)
        self.horizontalLayoutWidget.raise_()
        self.verticalLayoutWidget.raise_()
        self.rerollChk.raise_()
        self.labelP.raise_()
        self.labelRoll1.raise_()
        self.labelRoll2.raise_()
        self.labelRoll3.raise_()
        self.banner.raise_()
        self.setPlayer.raise_()
        self.onSGT.raise_()
        self.groupBox.raise_()
        MainWindow.setCentralWidget(self.randomGun)

        self.retranslateUi(MainWindow)
        self.slotP1.setCurrentRow(-1)
        self.slotP2.setCurrentRow(-1)
        self.slotP4.setCurrentRow(-1)
        self.slotP3.setCurrentRow(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.setMapE.clicked.connect(self.setMapEBtn)
        self.setMapM.clicked.connect(self.setMapMBtn)
        self.setMapS.clicked.connect(self.setMapSBtn)
        self.setMapK.clicked.connect(self.setMapKBtn)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "randomGun"))
        self.setMapE.setToolTip(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">에란겔</p></body></html>"))
        self.setRoll1.setText(_translate("MainWindow", " Easy"))
        self.setRoll2.setText(_translate("MainWindow", " Nomal"))
        self.setRoll3.setText(_translate("MainWindow", " Hard"))
        self.rerollChk.setText(_translate("MainWindow", "  중 복  제 거"))
        self.labelP.setText(_translate("MainWindow", "인원수 :"))
        self.labelRoll1.setText(_translate("MainWindow", "Easy    : 연사 1개, 연사+DMR+SR 1개"))
        self.labelRoll2.setText(_translate("MainWindow", "Nomal : 연사+DMR 1개, 연사+DMR+SR 1개"))
        self.labelRoll3.setText(_translate("MainWindow", "Hard   : ALL Random 2개"))
        self.onSGT.setText(_translate("MainWindow", "  샷건, 토미건 포함"))
        self.groupBox.setTitle(_translate("MainWindow", "Result"))
        self.Player1.setText(_translate("MainWindow", "P1"))
        self.slotP1.setSortingEnabled(False)
        self.Player2.setText(_translate("MainWindow", "P2"))
        self.slotP2.setSortingEnabled(False)
        self.Player4.setText(_translate("MainWindow", "P4"))
        self.slotP4.setSortingEnabled(False)
        self.Player3.setText(_translate("MainWindow", "P3"))
        self.slotP3.setSortingEnabled(False)

    # 맵 별 버튼 클릭 이벤트
    # 맵별 총기 리스트 셋팅(룰 + ModSGT 포함여부)
    def setMapEBtn(self):
        global Gun1
        global Gun2
        if self.setRoll1.isChecked():
            Gun1 = AR + SMG + ErangelAR
            Gun2 = SR + DMR + MISC + ErangelDMR
            if self.onSGT.isChecked() == True:
                Gun1 += ModSGT
        elif self.setRoll2.isChecked():
            Gun1 = AR + SMG + DMR + ErangelAR + ErangelDMR
            Gun2 = Gun1 + SR + MISC
            if self.onSGT.isChecked() == True:
                Gun1 += ModSGT
        elif self.setRoll3.isChecked():
            Gun1 = Gun2 = AR + SMG + SR + DMR + MISC + ErangelAR + ErangelDMR
            if self.onSGT.isChecked() == True:
                Gun1 += ModSGT
        self.resultBox()

    def setMapMBtn(self):
        global Gun1
        global Gun2
        if self.setRoll1.isChecked():
            Gun1 = AR + SMG + MiramarAR
            Gun2 = SR + DMR + MISC + MiramarDMR + MiramarSR
            if self.onSGT.isChecked() == True:
                Gun1 += ModSGT
        elif self.setRoll2.isChecked():
            Gun1 = AR + SMG + DMR + MiramarAR + MiramarDMR
            Gun2 = Gun1 + SR + MISC + MiramarSR
            if self.onSGT.isChecked() == True:
                Gun1 += ModSGT
        elif self.setRoll3.isChecked():
            Gun1 = Gun2 = AR + SMG + SR + DMR + MISC + MiramarAR + MiramarDMR + MiramarSR
            if self.onSGT.isChecked() == True:
                Gun1 += ModSGT
        self.resultBox()

    def setMapSBtn(self):
        global Gun1
        global Gun2
        if self.setRoll1.isChecked():
            Gun1 = AR + SMG + SanhokAR
            Gun2 = SR + DMR + MISC + SanhokDMR
            if self.onSGT.isChecked() == True:
                Gun1 += ModSGT
        elif self.setRoll2.isChecked():
            Gun1 = AR + SMG + DMR + SanhokAR + SanhokDMR
            Gun2 = Gun1 + SR + MISC
            if self.onSGT.isChecked() == True:
                Gun1 += ModSGT
        elif self.setRoll3.isChecked():
            Gun1 = Gun2 = AR + SMG + SR + DMR + MISC + SanhokAR + SanhokDMR
            if self.onSGT.isChecked() == True:
                Gun1 += ModSGT
        self.resultBox()

    def setMapKBtn(self):
        global Gun1
        global Gun2
        if self.setRoll1.isChecked():
            Gun1 = AR + SMG + KarakinAR
            Gun2 = SR + DMR + MISC + KarakinDMR + KarakinSR
            if self.onSGT.isChecked() == True:
                Gun1 += ModSGT
        elif self.setRoll2.isChecked():
            Gun1 = AR + SMG + DMR + KarakinAR + KarakinDMR
            Gun2 = Gun1 + SR + MISC + KarakinSR
            if self.onSGT.isChecked() == True:
                Gun1 += ModSGT
        elif self.setRoll3.isChecked():
            Gun1 = Gun2 = AR + SMG + SR + DMR + MISC + KarakinAR + KarakinDMR + KarakinSR
            if self.onSGT.isChecked() == True:
                Gun1 += ModSGT
        self.resultBox()

    # 랜덤 총기 결정
    def gachaGun(self):
        Slot1 = Slot2 = "-"
        Slot1 = random.choice(Gun1)

        # 중복 검사 옵션
        if self.rerollChk.isChecked() == True:
            Slot2 = random.choice(Gun2)
            while Slot1 == Slot2:
                Slot2 = random.choice(Gun2)
            return Slot1, Slot2
        else:
            Slot2 = random.choice(Gun2)
            return Slot1, Slot2

    # 가챠 결과 값 출력
    def resultBox(self):
        for i in range(self.setPlayer.value()):
            Slot1, Slot2 = self.gachaGun()
            if i == 0:
                self.slotP1.takeItem(0)
                self.slotP1.takeItem(0)
                self.slotP1.addItem(" Slot1 :  " + Slot1)
                self.slotP1.addItem(" Slot2 :  " + Slot2)
            elif i == 1:
                self.slotP2.takeItem(0)
                self.slotP2.takeItem(0)
                self.slotP2.addItem(" Slot1 :  " + Slot1)
                self.slotP2.addItem(" Slot2 :  " + Slot2)
            elif i == 2:
                self.slotP3.takeItem(0)
                self.slotP3.takeItem(0)
                self.slotP3.addItem(" Slot1 :  " + Slot1)
                self.slotP3.addItem(" Slot2 :  " + Slot2)
            elif i == 3:
                self.slotP4.takeItem(0)
                self.slotP4.takeItem(0)
                self.slotP4.addItem(" Slot1 :  " + Slot1)
                self.slotP4.addItem(" Slot2 :  " + Slot2)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
