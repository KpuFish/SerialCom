# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTextEdit, QWidget)

class Ui_MainWindow(object) :
    def setupUi(self, MainWindow) :
        if not MainWindow.objectName() :
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(802, 385)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 70, 149, 261))
        self.label.setPixmap(QPixmap(u"../img/STM32-Nucleo-F401RE-board.png"))
        self.label.setScaledContents(True)
        self.send = QPushButton(self.centralwidget)
        self.send.setObjectName(u"send")
        self.send.setGeometry(QRect(660, 24, 75, 31))
        self.rxline = QTextEdit(self.centralwidget)
        self.rxline.setObjectName(u"rxline")
        self.rxline.setGeometry(QRect(190, 70, 451, 261))
        self.rxline.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.current_comport = QComboBox(self.centralwidget)
        self.current_comport.setObjectName(u"current_comport")
        self.current_comport.setGeometry(QRect(660, 240, 68, 22))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(190, 10, 50, 16))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(190, 50, 50, 16))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(660, 220, 50, 16))
        font = QFont()
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.current_baudrate = QComboBox(self.centralwidget)
        self.current_baudrate.setObjectName(u"current_baudrate")
        self.current_baudrate.setGeometry(QRect(660, 300, 68, 22))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(660, 280, 61, 16))
        self.label_5.setFont(font)
        self.txline = QLineEdit(self.centralwidget)
        self.txline.setObjectName(u"txline")
        self.txline.setGeometry(QRect(190, 30, 451, 21))
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 50, 61, 16))
        self.pushButton_open = QPushButton(self.centralwidget)
        self.pushButton_open.setObjectName(u"pushButton_open")
        self.pushButton_open.setGeometry(QRect(660, 120, 75, 41))
        self.pushButton_close = QPushButton(self.centralwidget)
        self.pushButton_close.setObjectName(u"pushButton_close")
        self.pushButton_close.setGeometry(QRect(660, 170, 75, 41))
        self.pushButton_clear = QPushButton(self.centralwidget)
        self.pushButton_clear.setObjectName(u"pushButton_clear")
        self.pushButton_clear.setGeometry(QRect(660, 70, 75, 41))
        self.pushButton_scan = QPushButton(self.centralwidget)
        self.pushButton_scan.setObjectName(u"pushButton_scan")
        self.pushButton_scan.setGeometry(QRect(740, 235, 51, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 802, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow) :
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Serial Test", None))
        self.label.setText("")
        self.send.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TX", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"RX", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Com", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"BaudRate", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Target B/D", None))
        self.pushButton_open.setText(QCoreApplication.translate("MainWindow", u"OPEN", None))
        self.pushButton_close.setText(QCoreApplication.translate("MainWindow", u"CLOSE", None))
        self.pushButton_clear.setText(QCoreApplication.translate("MainWindow", u"RX CLEAR", None))
        self.pushButton_scan.setText(QCoreApplication.translate("MainWindow", u"SCAN", None))
    # retranslateUi

