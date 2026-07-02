from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtCore import QDate
from ui_dialog_buscar_partida import Ui_Dialog
from dialog_resultados import DialogResultados
from APIClient import APIClient
import sys
import os

src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(src_path)

from utils.Uteis import filtrar_nome

class DialogBuscarPartida(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.api_client = APIClient()
        self.setWindowTitle("Buscar Partida")
        self.setFixedSize(self.size())
        
        self.ui.dateEdit.setDate(QDate.currentDate())
        self.ui.dateEdit.setDisplayFormat("yyyy")

        self.ui.lineEdit.textChanged.connect(self.aplicar_filtro_nome)
        self.ui.lineEdit_2.textChanged.connect(self.aplicar_filtro_nome)
        
        self.popular_comboboxes()
        
        self.ui.pushButton.clicked.connect(self.buscar_partidas)
        self.ui.pushButton_2.clicked.connect(self.cancelar)
    
    def popular_comboboxes(self):
        resultados = ["", "1-0", "0-1", "1/2-1/2", "*"]
        self.ui.comboBox_4.addItems(resultados)
        
        terminacoes = [
            "", "Abandono", "Afogamento", "Xeque-mate", "Empate por acordo", 
            "Empate por repetição", "Empate por insuficiencia material", 
            "Empate por regra dos 50 lances", "Timeout", "Vitória por tempo"
        ]
        self.ui.comboBox_3.addItems(terminacoes)

    def aplicar_filtro_nome(self):
        sender = self.sender()
        
        if sender == self.ui.lineEdit:
            texto = self.ui.lineEdit.text()
            if texto:
                texto_filtrado = filtrar_nome(texto)
                if texto != texto_filtrado:
                    self.ui.lineEdit.setText(texto_filtrado)
        elif sender == self.ui.lineEdit_2:
            texto = self.ui.lineEdit_2.text()
            if texto:
                texto_filtrado = filtrar_nome(texto)
                if texto != texto_filtrado:
                    self.ui.lineEdit_2.setText(texto_filtrado)
    
    def buscar_partidas(self):
        try:
            filtros = {
                'jogador_brancas': self.ui.lineEdit.text().strip() or None,
                'jogador_pretas': self.ui.lineEdit_2.text().strip() or None,
                'terminacao': self.ui.comboBox_3.currentText() or None,
                'resultado': self.ui.comboBox_4.currentText() or None,
                'ano': self.ui.dateEdit.date().year() if self.ui.dateEdit.date().year() != QDate.currentDate().year() else None
            }
            
            filtros = {k: v for k, v in filtros.items() if v is not None}
            
            partidas = self.api_client.buscar_partidas_com_filtros(filtros)
            
            if partidas:
                dialog_resultados = DialogResultados(self, partidas, tipo="partidas")
                self.accept() 
                dialog_resultados.exec()
            else:
                QMessageBox.information(self, "Busca", "Nenhuma partida encontrada com os filtros especificados.")
                
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro na busca: {str(e)}")
    
    def cancelar(self):
        self.reject()