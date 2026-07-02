# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_cadastrar_jogador.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(293, 354)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 60, 61, 21))
        font = QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(80, 60, 191, 22))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 100, 51, 21))
        self.label_2.setFont(font)
        self.lineEdit_2 = QLineEdit(Dialog)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(80, 100, 191, 22))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 180, 81, 21))
        self.label_3.setFont(font)
        self.comboBox = QComboBox(Dialog)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(110, 180, 101, 22))
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 220, 101, 21))
        self.label_4.setFont(font)
        self.lineEdit_3 = QLineEdit(Dialog)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(130, 220, 81, 22))
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 140, 151, 21))
        self.label_5.setFont(font)
        self.dateEdit = QDateEdit(Dialog)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(180, 140, 91, 22))
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 260, 111, 21))
        self.label_6.setFont(font)
        self.comboBox_2 = QComboBox(Dialog)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(130, 260, 81, 22))
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(40, 300, 91, 31))
        font1 = QFont()
        font1.setPointSize(12)
        self.pushButton.setFont(font1)
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(160, 300, 101, 31))
        self.pushButton_2.setFont(font1)
        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 20, 171, 16))
        font2 = QFont()
        font2.setPointSize(14)
        self.label_7.setFont(font2)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Nome:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Email:", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Federa\u00e7\u00e3o:", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Rating inicial:", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Data de nascimento:", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Titula\u00e7\u00e3o FIDE:", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u2705 Salvar", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"\u274c Cancelar", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Dados de cadastro", None))
    # retranslateUi

