# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_visualizar_jogador.ui'
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
        Dialog.resize(345, 408)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 49, 16))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 20, 51, 21))
        font = QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(80, 20, 241, 22))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 50, 51, 21))
        self.label_3.setFont(font)
        self.lineEdit_2 = QLineEdit(Dialog)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(80, 50, 241, 22))
        self.label_data_nascimento = QLabel(Dialog)
        self.label_data_nascimento.setObjectName(u"label_data_nascimento")
        self.label_data_nascimento.setGeometry(QRect(20, 170, 301, 21))
        self.label_data_nascimento.setFont(font)
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 80, 81, 21))
        self.label_4.setFont(font)
        self.comboBox = QComboBox(Dialog)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(100, 80, 91, 22))
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 110, 111, 21))
        self.label_6.setFont(font)
        self.comboBox_2 = QComboBox(Dialog)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(130, 110, 71, 22))
        self.label_rating = QLabel(Dialog)
        self.label_rating.setObjectName(u"label_rating")
        self.label_rating.setGeometry(QRect(20, 140, 301, 21))
        self.label_rating.setFont(font)
        self.label_data_cadastro = QLabel(Dialog)
        self.label_data_cadastro.setObjectName(u"label_data_cadastro")
        self.label_data_cadastro.setGeometry(QRect(20, 200, 301, 21))
        self.label_data_cadastro.setFont(font)
        self.label_9 = QLabel(Dialog)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 230, 111, 21))
        self.label_9.setFont(font)
        self.label_vitorias = QLabel(Dialog)
        self.label_vitorias.setObjectName(u"label_vitorias")
        self.label_vitorias.setGeometry(QRect(20, 260, 301, 21))
        self.label_vitorias.setFont(font)
        self.label_empates = QLabel(Dialog)
        self.label_empates.setObjectName(u"label_empates")
        self.label_empates.setGeometry(QRect(20, 290, 301, 21))
        self.label_empates.setFont(font)
        self.label_derrotas = QLabel(Dialog)
        self.label_derrotas.setObjectName(u"label_derrotas")
        self.label_derrotas.setGeometry(QRect(20, 320, 301, 21))
        self.label_derrotas.setFont(font)
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 360, 81, 31))
        self.pushButton.setFont(font)
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(130, 360, 81, 31))
        self.pushButton_2.setFont(font)
        self.pushButton_3 = QPushButton(Dialog)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(240, 360, 81, 31))
        self.pushButton_3.setFont(font)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Nome:", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Email:", None))
        self.label_data_nascimento.setText(QCoreApplication.translate("Dialog", u"Data de Nascimento:", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Federa\u00e7\u00e3o:", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Titula\u00e7\u00e3o FIDE:", None))
        self.label_rating.setText(QCoreApplication.translate("Dialog", u"Rating: ", None))
        self.label_data_cadastro.setText(QCoreApplication.translate("Dialog", u"Data de Cadastro:", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Estat\u00edsticas (%):", None))
        self.label_vitorias.setText(QCoreApplication.translate("Dialog", u"Vit\u00f3rias: ", None))
        self.label_empates.setText(QCoreApplication.translate("Dialog", u"Empates:", None))
        self.label_derrotas.setText(QCoreApplication.translate("Dialog", u"Derrotas:", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\U0001f5d1\U0000fe0f Excluir", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"\u270f\ufe0f Editar", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"\u2705 Ok", None))
    # retranslateUi

