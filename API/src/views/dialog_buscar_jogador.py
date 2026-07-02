from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtCore import QThread, Signal
from ui_dialog_buscar_jogador import Ui_Dialog
from dialog_resultados import DialogResultados
from APIClient import APIClient
import sys
import os

src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(src_path)
print(f"SRC path adicionado: {src_path}")

from utils.Uteis import (
    TITULOS_FIDE, FEDERACOES_FIDE, validar_numero_positivo,
    filtrar_nome, filtrar_email, filtrar_numero_positivo  
)

class BuscarJogadorThread(QThread):
    
    finished_signal = Signal(list)
    error_signal = Signal(str)
    
    def __init__(self, api_client, filtros):
        super().__init__()
        self.api_client = api_client
        self.filtros = filtros
    
    def run(self):
        try:
            resultados = self.api_client.buscar_jogadores(self.filtros)
            self.finished_signal.emit(resultados)
        except Exception as e:
            self.error_signal.emit(str(e))

class DialogBuscarJogador(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.api_client = APIClient()
        
        self.ui.pushButton.clicked.connect(self.buscar_jogador)
        self.ui.pushButton_2.clicked.connect(self.cancelar)
        self.setFixedSize(self.size())
        self.ui.lineEdit.textChanged.connect(self.aplicar_filtro_nome)
        self.ui.lineEdit_2.textChanged.connect(self.aplicar_filtro_email)
        self.ui.lineEdit_3.textChanged.connect(self.aplicar_filtro_idade_min)
        self.ui.lineEdit_3.setMaxLength(3)
        self.ui.lineEdit_4.textChanged.connect(self.aplicar_filtro_idade_max)
        self.ui.lineEdit_4.setMaxLength(3)

        self.setWindowTitle("Buscar jogador")

        self.popular_combobox()
        self.verificar_conexao()
    
    def verificar_conexao(self):
        if not self.api_client.testar_conexao():
            QMessageBox.warning(
                self, 
                "Conexão", 
                "Não foi possível conectar à API. Verifique se o servidor Flask está rodando na porta 5000."
            )
    
    def popular_combobox(self):
        titulos = [""] + TITULOS_FIDE  
        self.ui.comboBox.addItems(titulos)
        
        federacoes_ordenadas = sorted(FEDERACOES_FIDE)
        federacoes = [""] + federacoes_ordenadas  
        self.ui.comboBox_2.addItems(federacoes)
    
    def buscar_jogador(self):
        filtros = {
            'nome': self.ui.lineEdit.text().strip(),
            'email': self.ui.lineEdit_2.text().strip(),
            'titulo_fide': self.ui.comboBox.currentText(),
            'federacao': self.ui.comboBox_2.currentText()
        }
        
        idade_min = self.ui.lineEdit_3.text().strip()
        idade_max = self.ui.lineEdit_4.text().strip()

        if idade_min:
            if not validar_numero_positivo(idade_min):
                QMessageBox.warning(self, "Idade Inválida", "Idade mínima deve ser um número positivo.")
                return

            filtros['idade_min'] = idade_min
        
        if idade_max:
            if not validar_numero_positivo(idade_max):
                QMessageBox.warning(self, "Idade Inválida", "Idade máxima deve ser um número positivo.")
                return

            filtros['idade_max'] = idade_max
        
        if idade_min and idade_max:
            if int(idade_min) > int(idade_max):
                QMessageBox.warning(self, "Idade Inválida", "Idade mínima não pode ser maior que idade máxima.")
                return
            
        filtros = {k: v for k, v in filtros.items() if v}
        
        self.ui.pushButton.setEnabled(False)
        self.ui.pushButton.setText("Buscando...")
        
        self.busca_thread = BuscarJogadorThread(self.api_client, filtros)
        self.busca_thread.finished_signal.connect(self.on_busca_finished)
        self.busca_thread.error_signal.connect(self.on_busca_error)
        self.busca_thread.start()
    
    def on_busca_finished(self, resultados):
        self.ui.pushButton.setEnabled(True)
        self.ui.pushButton.setText("🔍 Buscar")
        
        if resultados:
            dialog_resultados = DialogResultados(self, resultados, tipo="jogadores")
            dialog_resultados.exec()  
        
        else:
            QMessageBox.information(self, "Busca", "Nenhum jogador encontrado com os filtros especificados.")
    
    def on_busca_error(self, erro):
        self.ui.pushButton.setEnabled(True)
        self.ui.pushButton.setText("🔍 Buscar")
        
        QMessageBox.critical(self, "Erro na Busca", f"Erro ao buscar jogadores:\n{erro}")
    
    def cancelar(self):
        if hasattr(self, 'busca_thread') and self.busca_thread.isRunning():
            self.busca_thread.terminate()
            self.busca_thread.wait()
        
        self.reject()

    def aplicar_filtro_nome(self):
        texto = self.ui.lineEdit.text()
        if texto:
            self.ui.lineEdit.setText(filtrar_nome(texto))
    
    def aplicar_filtro_email(self):
        texto = self.ui.lineEdit_2.text()
        if texto:
            self.ui.lineEdit_2.setText(filtrar_email(texto))

    def aplicar_filtro_idade_min(self):

        texto = self.ui.lineEdit_3.text()
        if texto:
            self.ui.lineEdit_3.setText(filtrar_numero_positivo(texto))

    def aplicar_filtro_idade_max(self):

        texto = self.ui.lineEdit_4.text()
        if texto:
            self.ui.lineEdit_4.setText(filtrar_numero_positivo(texto))