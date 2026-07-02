# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_buscar_partida.ui'
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
        Dialog.resize(332, 279)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 60, 61, 16))
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 100, 61, 16))
        self.label_2.setFont(font)
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 180, 81, 16))
        self.label_3.setFont(font)
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 140, 91, 20))
        self.label_4.setFont(font)
        self.comboBox_3 = QComboBox(Dialog)
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setGeometry(QRect(110, 140, 201, 22))
        self.comboBox_4 = QComboBox(Dialog)
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setGeometry(QRect(100, 180, 101, 22))
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(220, 180, 41, 16))
        self.label_5.setFont(font)
        self.dateEdit = QDateEdit(Dialog)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(260, 180, 51, 22))
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 10, 131, 31))
        font1 = QFont()
        font1.setPointSize(14)
        self.label_6.setFont(font1)
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(90, 60, 221, 22))
        self.lineEdit_2 = QLineEdit(Dialog)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(90, 100, 221, 22))
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(40, 230, 101, 31))
        self.pushButton.setFont(font)
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(180, 230, 101, 31))
        self.pushButton_2.setFont(font)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Brancas:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Pretas:", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Resultado:", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Termina\u00e7\u00e3o:", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Ano:", None))
        self.dateEdit.setDisplayFormat(QCoreApplication.translate("Dialog", u"yyyy", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Buscar partida", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\U0001f50d Buscar ", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"\u274c Cancelar", None))
    # retranslateUi

