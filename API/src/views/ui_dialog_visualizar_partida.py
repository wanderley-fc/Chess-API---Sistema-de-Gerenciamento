# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_visualizar_partida.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QTextEdit, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(500, 600)
        self.label_jogadores = QLabel(Dialog)
        self.label_jogadores.setObjectName(u"label_jogadores")
        self.label_jogadores.setGeometry(QRect(20, 20, 460, 30))
        font = QFont()
        font.setPointSize(14)
        font.setBold(False)
        self.label_jogadores.setFont(font)
        self.label_resultado = QLabel(Dialog)
        self.label_resultado.setObjectName(u"label_resultado")
        self.label_resultado.setGeometry(QRect(20, 60, 460, 25))
        font1 = QFont()
        font1.setPointSize(11)
        self.label_resultado.setFont(font1)
        self.label_evento_local = QLabel(Dialog)
        self.label_evento_local.setObjectName(u"label_evento_local")
        self.label_evento_local.setGeometry(QRect(20, 90, 460, 25))
        self.label_evento_local.setFont(font1)
        self.label_data = QLabel(Dialog)
        self.label_data.setObjectName(u"label_data")
        self.label_data.setGeometry(QRect(20, 120, 460, 25))
        self.label_data.setFont(font1)
        self.label_detalhes = QLabel(Dialog)
        self.label_detalhes.setObjectName(u"label_detalhes")
        self.label_detalhes.setGeometry(QRect(20, 150, 460, 25))
        self.label_detalhes.setFont(font1)
        self.label_lances_titulo = QLabel(Dialog)
        self.label_lances_titulo.setObjectName(u"label_lances_titulo")
        self.label_lances_titulo.setGeometry(QRect(20, 190, 200, 25))
        self.label_lances_titulo.setFont(font1)
        self.textEdit_lances = QTextEdit(Dialog)
        self.textEdit_lances.setObjectName(u"textEdit_lances")
        self.textEdit_lances.setGeometry(QRect(20, 220, 460, 300))
        font2 = QFont()
        font2.setFamilies([u"Courier"])
        font2.setPointSize(9)
        self.textEdit_lances.setFont(font2)
        self.textEdit_lances.setReadOnly(True)
        self.btn_excluir = QPushButton(Dialog)
        self.btn_excluir.setObjectName(u"btn_excluir")
        self.btn_excluir.setGeometry(QRect(270, 540, 100, 41))
        font3 = QFont()
        font3.setPointSize(12)
        self.btn_excluir.setFont(font3)
        self.btn_ok = QPushButton(Dialog)
        self.btn_ok.setObjectName(u"btn_ok")
        self.btn_ok.setGeometry(QRect(389, 540, 91, 41))
        self.btn_ok.setFont(font3)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Visualizar Partida", None))
        self.label_jogadores.setText(QCoreApplication.translate("Dialog", u"Jogador Brancas vs Jogador Pretas", None))
        self.label_resultado.setText(QCoreApplication.translate("Dialog", u"Resultado: ", None))
        self.label_evento_local.setText(QCoreApplication.translate("Dialog", u"Evento:  - Local: ", None))
        self.label_data.setText(QCoreApplication.translate("Dialog", u"Data: ", None))
        self.label_detalhes.setText(QCoreApplication.translate("Dialog", u"Termina\u00e7\u00e3o:  | Tempo:  | Rodada: ", None))
        self.label_lances_titulo.setText(QCoreApplication.translate("Dialog", u"Lances:", None))
        self.btn_excluir.setText(QCoreApplication.translate("Dialog", u"\U0001f5d1\U0000fe0f Excluir", None))
        self.btn_ok.setText(QCoreApplication.translate("Dialog", u"\u2705 OK", None))
    # retranslateUi

