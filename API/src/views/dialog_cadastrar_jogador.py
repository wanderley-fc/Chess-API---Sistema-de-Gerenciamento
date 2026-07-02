from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtCore import QDate
from ui_dialog_cadastrar_jogador import Ui_Dialog
from APIClient import APIClient
import sys
import os

src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(src_path)

from utils.Uteis import (
    FEDERACOES_FIDE, TITULOS_FIDE, validar_nome, validar_email, 
    validar_rating, validar_federacao, validar_titulo_fide,
    filtrar_nome, filtrar_email, filtrar_numero_positivo,
    RATING_MINIMO, RATING_MAXIMO
)

class DialogCadastrarJogador(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.api_client = APIClient()
        
        self.setFixedSize(self.size())
        self.ui.lineEdit_3.setMaxLength(4)

        data_padrao = QDate.currentDate().addYears(-18)
        self.ui.dateEdit.setDate(data_padrao)
        
        self.popular_comboboxes()
        
        self.ui.pushButton.clicked.connect(self.salvar_jogador)
        self.ui.pushButton_2.clicked.connect(self.cancelar)
        
        self.ui.lineEdit.textChanged.connect(self.aplicar_filtro_nome)
        self.ui.lineEdit_2.textChanged.connect(self.aplicar_filtro_email)
        self.ui.lineEdit_3.textChanged.connect(self.aplicar_filtro_rating)

        self.setWindowTitle("Cadastrar jogador")
    
    def popular_comboboxes(self):
        federacoes_ordenadas = sorted(FEDERACOES_FIDE)
        federacoes = [""] + federacoes_ordenadas
        self.ui.comboBox.addItems(federacoes)
        
        titulos = [""] + TITULOS_FIDE
        self.ui.comboBox_2.addItems(titulos)
    
    def aplicar_filtro_nome(self):
        texto = self.ui.lineEdit.text()
        if texto:
            self.ui.lineEdit.setText(filtrar_nome(texto))
    
    def aplicar_filtro_email(self):
        texto = self.ui.lineEdit_2.text()
        if texto:
            self.ui.lineEdit_2.setText(filtrar_email(texto))
    
    def aplicar_filtro_rating(self):
        texto = self.ui.lineEdit_3.text()
        if texto:
            self.ui.lineEdit_3.setText(filtrar_numero_positivo(texto))
    
    def salvar_jogador(self):
        try:
            dados_jogador = self.get_dados_jogador()
            
            if not self.validar_dados(dados_jogador):
                return
            
            resultado = self.api_client.cadastrar_jogador(dados_jogador)
            
            QMessageBox.information(self, "Sucesso", "Jogador cadastrado com sucesso!")
            self.accept()
            
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao cadastrar jogador: {str(e)}")
    
    def validar_dados(self, dados):
        if not dados['nome']:
            QMessageBox.warning(self, "Aviso", "O nome é obrigatório!")
            self.ui.lineEdit.setFocus()
            return False
        
        if not validar_nome(dados['nome']):
            QMessageBox.warning(self, "Aviso", "Nome deve conter apenas letras e espaços!")
            self.ui.lineEdit.setFocus()
            return False
        
        if not dados['email']:
            QMessageBox.warning(self, "Aviso", "O email é obrigatório!")
            self.ui.lineEdit_2.setFocus()
            return False
        
        if not validar_email(dados['email']):
            QMessageBox.warning(self, "Aviso", "Por favor, insira um email válido!")
            self.ui.lineEdit_2.setFocus()
            return False
    
        if dados['federacao'] and not validar_federacao(dados['federacao']):
            QMessageBox.warning(self, "Aviso", "Federação inválida!")
            self.ui.comboBox.setFocus()
            return False
        
        if dados['rating'] is not None:
            if not validar_rating(dados['rating']):
                QMessageBox.warning(self, "Aviso", f"Rating deve estar entre {RATING_MINIMO} e {RATING_MAXIMO}!")
                self.ui.lineEdit_3.setFocus()
                return False
        
        if dados['titulo_fide'] and not validar_titulo_fide(dados['titulo_fide']):
            QMessageBox.warning(self, "Aviso", "Título FIDE inválido!")
            self.ui.comboBox_2.setFocus()
            return False
        
        if self.ui.dateEdit.date() > QDate.currentDate():
            QMessageBox.warning(self, "Aviso", "A data de nascimento não pode ser no futuro!")
            self.ui.dateEdit.setFocus()
            return False
        
        return True
    
    def cancelar(self):
        self.reject()
    
    def get_dados_jogador(self):
        federacao = self.ui.comboBox.currentText().strip()
        rating_text = self.ui.lineEdit_3.text().strip()
        
        qdate = self.ui.dateEdit.date()
        data_nascimento = f"{qdate.year()}-{qdate.month():02d}-{qdate.day():02d}"
        
        dados = {
            'nome': self.ui.lineEdit.text().strip(),
            'email': self.ui.lineEdit_2.text().strip(),
            'federacao': federacao if federacao else None, 
            'rating': int(rating_text) if rating_text else 1500,
            'data_nascimento': data_nascimento,
            'titulo_fide': self.ui.comboBox_2.currentText() or None
        }
        
        return dados