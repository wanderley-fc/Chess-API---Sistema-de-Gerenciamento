from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtCore import QDate
from ui_dialog_cadastrar_partida import Ui_Dialog
from APIClient import APIClient
import sys
import os

src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(src_path)

from utils.Uteis import (
    RESULTADOS_VALIDOS, TERMINACOES_VALIDAS, validar_resultado, validar_terminacao
)

class DialogCadastrarPartida(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.api_client = APIClient()
        
        self.setFixedSize(self.size())
        self.ui.dateEdit.setDate(QDate.currentDate())
        self.popular_comboboxes()
        self.carregar_jogadores()

        self.ui.pushButton_2.clicked.connect(self.salvar_partida)  
        self.ui.pushButton.clicked.connect(self.cancelar)  
        self.ui.lineEdit_3.textChanged.connect(self.aplicar_filtro_time_control)
        
        self.setWindowTitle("Cadastrar Partida")

    def popular_comboboxes(self):
        resultados = [""] + RESULTADOS_VALIDOS
        self.ui.comboBox_3.addItems(resultados)
 
        terminacoes = [""] + TERMINACOES_VALIDAS
        self.ui.comboBox_4.addItems(terminacoes)

    def aplicar_filtro_time_control(self):
        texto = self.ui.lineEdit_3.text()
        if texto:
            texto_filtrado = ''.join(c for c in texto if c in '0123456789+')
            if texto_filtrado != texto:
                self.ui.lineEdit_3.setText(texto_filtrado)

    def carregar_jogadores(self):
        try:
            jogadores = self.api_client.buscar_jogadores({})
            
            opcoes_jogadores = [""] 
            
            for jogador in jogadores:
                nome = jogador.get('nome', '')
                if nome:
                    opcoes_jogadores.append(nome)

            self.ui.comboBox.addItems(opcoes_jogadores)
            self.ui.comboBox_2.addItems(opcoes_jogadores)
            
        except Exception as e:
            print(f"Erro ao carregar jogadores: {e}")

    def salvar_partida(self):
        try:
            dados_partida = self.get_dados_partida()

            if not self.validar_dados(dados_partida):
                return
            
            resultado = self.api_client.cadastrar_partida(dados_partida)
            
            if resultado:
                QMessageBox.information(self, "Sucesso", "Partida cadastrada com sucesso!")
                self.accept()
            else:
                QMessageBox.critical(self, "Erro", "Erro ao cadastrar partida na API!")
            
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao salvar partida: {str(e)}")

    def get_dados_partida(self):
        return {
            'jogador_brancas': self.ui.comboBox.currentText(),
            'jogador_pretas': self.ui.comboBox_2.currentText(),
            'evento': self.ui.lineEdit.text().strip(),
            'local_evento': self.ui.lineEdit_2.text().strip(),
            'data_partida': self.ui.dateEdit.date().toString("yyyy-MM-dd"),
            'resultado': self.ui.comboBox_3.currentText() or None,
            'terminacao': self.ui.comboBox_4.currentText() or None,
            'controle_tempo': self.ui.lineEdit_3.text().strip() or None,
            'rodada': self.ui.lineEdit_4.text().strip() or None,
            'lances': self.ui.plainTextEdit.toPlainText().strip() or None
        }

    def validar_dados(self, dados):
        if not dados['jogador_brancas']:
            QMessageBox.warning(self, "Aviso", "Selecione o jogador das Brancas!")
            self.ui.comboBox.setFocus()
            return False
        
        if not dados['jogador_pretas']:
            QMessageBox.warning(self, "Aviso", "Selecione o jogador das Pretas!")
            self.ui.comboBox_2.setFocus()
            return False

        if dados['jogador_brancas'] == dados['jogador_pretas']:
            QMessageBox.warning(self, "Aviso", "Os jogadores não podem ser os mesmos!")
            return False
 
        if self.ui.dateEdit.date() > QDate.currentDate():
            QMessageBox.warning(self, "Aviso", "A data da partida não pode ser no futuro!")
            self.ui.dateEdit.setFocus()
            return False

        data_partida = self.ui.dateEdit.date()
        
        if not self.validar_data_nascimento_jogador(dados['jogador_brancas'], data_partida, "brancas"):
            return False
   
        if not self.validar_data_nascimento_jogador(dados['jogador_pretas'], data_partida, "pretas"):
            return False

        if dados['resultado'] and not validar_resultado(dados['resultado']):
            QMessageBox.warning(self, "Aviso", f"Resultado inválido! Resultados válidos: {', '.join(RESULTADOS_VALIDOS)}")
            self.ui.comboBox_3.setFocus()
            return False

        if dados['terminacao'] and not validar_terminacao(dados['terminacao']):
            QMessageBox.warning(self, "Aviso", f"Terminação inválida! Terminações válidas: {', '.join(TERMINACOES_VALIDAS)}")
            self.ui.comboBox_4.setFocus()
            return False
        
        return True

    def validar_data_nascimento_jogador(self, nome_jogador, data_partida, cor):
        try:
            jogadores = self.api_client.buscar_jogadores({'nome': nome_jogador})
            
            if not jogadores:
                QMessageBox.warning(self, "Aviso", f"Jogador das {cor} ('{nome_jogador}') não encontrado!")
                return False
            
            jogador = jogadores[0]
            
            if jogador.get('data_nascimento'):
                data_nascimento = QDate.fromString(jogador['data_nascimento'], "yyyy-MM-dd")
                
                if data_partida < data_nascimento:
                    QMessageBox.warning(
                        self, 
                        "Data Inválida", 
                        f"Data da partida ({data_partida.toString('dd/MM/yyyy')}) é anterior à\n"
                        f"data de nascimento de {jogador['nome']} ({data_nascimento.toString('dd/MM/yyyy')})"
                    )
                    self.ui.dateEdit.setFocus()
                    return False
            
            return True
            
        except Exception as e:
            print(f"Erro ao validar data de nascimento: {e}")
            return True

    def cancelar(self):
        self.reject()