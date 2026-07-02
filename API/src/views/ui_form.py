# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QApplication, QListView, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainFrame(object):
    def setupUi(self, MainFrame):
        if not MainFrame.objectName():
            MainFrame.setObjectName(u"MainFrame")
        MainFrame.resize(472, 544)
        self.centralwidget = QWidget(MainFrame)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 10, 201, 51))
        font = QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(20, 70, 201, 51))
        self.pushButton_2.setFont(font)
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(250, 10, 201, 51))
        self.pushButton_3.setFont(font)
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(250, 70, 201, 51))
        self.pushButton_4.setFont(font)
        self.listView = QListView(self.centralwidget)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(20, 130, 431, 371))
        MainFrame.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainFrame)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 472, 22))
        MainFrame.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainFrame)
        self.statusbar.setObjectName(u"statusbar")
        MainFrame.setStatusBar(self.statusbar)

        self.retranslateUi(MainFrame)

        QMetaObject.connectSlotsByName(MainFrame)
    # setupUi

    def retranslateUi(self, MainFrame):
        MainFrame.setWindowTitle(QCoreApplication.translate("MainFrame", u"MainFrame", None))
        self.pushButton.setText(QCoreApplication.translate("MainFrame", u"\u2654 Cadastrar Jogador", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainFrame", u"\u2656 Buscar Jogador", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainFrame", u"\u265b Cadastrar Partida", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainFrame", u"\u265e Buscar Partida", None))
    # retranslateUi

