# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_buscar_jogador.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(311, 329)
        Dialog.setStyleSheet(u"")
        self.comboBox = QComboBox(Dialog)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(120, 180, 71, 22))
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(80, 60, 201, 21))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 60, 61, 16))
        font = QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 100, 51, 16))
        self.label_2.setFont(font)
        self.lineEdit_2 = QLineEdit(Dialog)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(80, 100, 201, 21))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 140, 51, 16))
        self.label_3.setFont(font)
        self.lineEdit_3 = QLineEdit(Dialog)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(120, 140, 51, 21))
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(80, 140, 41, 20))
        self.label_4.setFont(font)
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(190, 140, 41, 20))
        self.label_5.setFont(font)
        self.lineEdit_4 = QLineEdit(Dialog)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(230, 140, 51, 21))
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 180, 91, 16))
        self.label_6.setFont(font)
        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 220, 91, 16))
        self.label_7.setFont(font)
        self.comboBox_2 = QComboBox(Dialog)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(120, 220, 71, 22))
        self.label_8 = QLabel(Dialog)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 10, 161, 31))
        font1 = QFont()
        font1.setPointSize(14)
        self.label_8.setFont(font1)
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(40, 270, 91, 31))
        font2 = QFont()
        font2.setPointSize(12)
        self.pushButton.setFont(font2)
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(170, 270, 101, 31))
        self.pushButton_2.setFont(font2)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Nome:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Email:", None))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Dialog", u"Email completo", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Idade:", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Min", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"M\u00e1x", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"T\u00edtulo FIDE:", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Federa\u00e7\u00e3o:", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Buscar Jogador", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\U0001f50d Buscar", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"\u274c Cancelar", None))
    # retranslateUi

