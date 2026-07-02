# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_cadastrar_partida.ui'
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
    QLabel, QLineEdit, QPlainTextEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(664, 422)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 61, 16))
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.comboBox = QComboBox(Dialog)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(90, 20, 221, 22))
        self.comboBox.setEditable(True)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 50, 61, 16))
        self.label_2.setFont(font)
        self.comboBox_2 = QComboBox(Dialog)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(90, 50, 221, 22))
        self.comboBox_2.setEditable(True)
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(350, 20, 61, 16))
        self.label_3.setFont(font)
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(420, 20, 221, 22))
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(350, 50, 61, 16))
        self.label_4.setFont(font)
        self.lineEdit_2 = QLineEdit(Dialog)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(420, 50, 221, 22))
        self.dateEdit = QDateEdit(Dialog)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(440, 140, 111, 22))
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(350, 140, 41, 16))
        self.label_5.setFont(font)
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(350, 110, 81, 16))
        self.label_6.setFont(font)
        self.comboBox_3 = QComboBox(Dialog)
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setGeometry(QRect(440, 110, 111, 22))
        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(350, 80, 81, 16))
        self.label_7.setFont(font)
        self.comboBox_4 = QComboBox(Dialog)
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setGeometry(QRect(440, 80, 201, 22))
        self.label_8 = QLabel(Dialog)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 80, 141, 16))
        self.label_8.setFont(font)
        self.lineEdit_3 = QLineEdit(Dialog)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(160, 80, 151, 22))
        self.label_9 = QLabel(Dialog)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 110, 61, 16))
        self.label_9.setFont(font)
        self.lineEdit_4 = QLineEdit(Dialog)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(90, 110, 221, 22))
        self.plainTextEdit = QPlainTextEdit(Dialog)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(20, 170, 621, 201))
        self.label_10 = QLabel(Dialog)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 140, 61, 16))
        self.label_10.setFont(font)
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(540, 380, 101, 31))
        self.pushButton.setFont(font)
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(420, 380, 101, 31))
        self.pushButton_2.setFont(font)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Brancas:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Pretas:", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Evento:", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Local:", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Data:", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Resultado:", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Termina\u00e7\u00e3o:", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Controle de tempo:", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Rodada:", None))
        self.plainTextEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"Digite os lances em nota\u00e7\u00e3o alg\u00e9brica... Ex: 1.e4e5 2.Nf3Nc6", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"Lances:", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u274c Cancelar", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"\u2705 Salvar", None))
    # retranslateUi

