from PySide6.QtWidgets import QDialog, QMessageBox
from ui_dialog_visualizar_jogador import Ui_Dialog
from datetime import datetime, date
from APIClient import APIClient
import sys
import os

src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(src_path)
from utils.Uteis import calcular_idade, FEDERACOES_FIDE, TITULOS_FIDE, filtrar_nome, filtrar_email

class DialogVisualizarJogador(QDialog):
    def __init__(self, parent=None, jogador_data=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setFixedSize(self.size())
        
        self.jogador_data = jogador_data
        self.modo_edicao = False
        
        self.ui.pushButton.clicked.connect(self.excluir_jogador)
        self.ui.pushButton_2.clicked.connect(self.toggle_edicao)
        self.ui.pushButton_3.clicked.connect(self.fechar)
        
        self.ui.lineEdit.textChanged.connect(self.aplicar_filtro_nome)
        self.ui.lineEdit_2.textChanged.connect(self.aplicar_filtro_email)
        
        self.popular_comboboxes()
        self.api_client = APIClient()
        
        if jogador_data:
            self.carregar_dados_jogador()
        
        self.toggle_campos_edicao(False)
    
    def aplicar_filtro_nome(self):
        texto = self.ui.lineEdit.text()
        if texto:
            self.ui.lineEdit.setText(filtrar_nome(texto))
    
    def aplicar_filtro_email(self):
        texto = self.ui.lineEdit_2.text()
        if texto:
            self.ui.lineEdit_2.setText(filtrar_email(texto))
    
    def popular_comboboxes(self):
        titulos = [""] + TITULOS_FIDE
        self.ui.comboBox_2.clear()
        self.ui.comboBox_2.addItems(titulos)
        
        federacoes_ordenadas = [""] + sorted(FEDERACOES_FIDE)
        self.ui.comboBox.clear()
        self.ui.comboBox.addItems(federacoes_ordenadas)
    
    def carregar_dados_jogador(self):
        if not self.jogador_data:
            return
        
        self.ui.lineEdit.setText(self.jogador_data.get('nome', ''))
        self.ui.lineEdit_2.setText(self.jogador_data.get('email', ''))
        
        rating = self.jogador_data.get('rating', '')
        self.ui.label_rating.setText(f"Rating: {rating}")
        
        data_nascimento = self.jogador_data.get('data_nascimento', '')
        if data_nascimento:
            data_nasc = datetime.strptime(data_nascimento, '%Y-%m-%d').date()
            data_formatada = data_nasc.strftime('%d/%m/%Y')
            idade = calcular_idade(data_nasc)
            self.ui.label_data_nascimento.setText(f"Data de Nascimento: {data_formatada} ({idade} anos)")
        else:
            self.ui.label_data_nascimento.setText("Data de Nascimento: N/A")
        
        data_cadastro = self.jogador_data.get('data_cadastro', '')
        if data_cadastro:
            data_cad = datetime.strptime(data_cadastro, '%Y-%m-%d').date()
            data_cad_formatada = data_cad.strftime('%d/%m/%Y')
            self.ui.label_data_cadastro.setText(f"Data de Cadastro: {data_cad_formatada}")
        else:
            self.ui.label_data_cadastro.setText("Data de Cadastro: N/A")
        
        federacao = self.jogador_data.get('federacao')
        titulo = self.jogador_data.get('titulo_fide')
        
        self.ui.comboBox.setCurrentText(federacao)
        self.ui.comboBox_2.setCurrentText(titulo)
        
        self.carregar_estatisticas()
    
    def carregar_estatisticas(self):
        jogador_id = self.jogador_data.get('id', 0)
        
        try:
            estatisticas = self.api_client.get_estatisticas(jogador_id)
            
            if estatisticas:
                total_partidas = estatisticas.get('total_partidas', 0)
                vitorias = estatisticas.get('vitorias', 0)
                empates = estatisticas.get('empates', 0)
                derrotas = estatisticas.get('derrotas', 0)
            else:
                total_partidas = vitorias = empates = derrotas = 0
                
        except Exception as e:
            print(f"Erro ao carregar estatísticas: {e}")
            total_partidas = vitorias = empates = derrotas = 0
        
        if total_partidas > 0:
            pct_vitorias = (vitorias / total_partidas) * 100
            pct_empates = (empates / total_partidas) * 100
            pct_derrotas = (derrotas / total_partidas) * 100
        else:
            pct_vitorias = pct_empates = pct_derrotas = 0
        
        self.ui.label_vitorias.setText(f"Vitórias: {pct_vitorias:.1f}% ({vitorias}/{total_partidas})")
        self.ui.label_empates.setText(f"Empates: {pct_empates:.1f}% ({empates}/{total_partidas})")
        self.ui.label_derrotas.setText(f"Derrotas: {pct_derrotas:.1f}% ({derrotas}/{total_partidas})")
    
    def toggle_edicao(self):
        if self.modo_edicao:
            if self.salvar_alteracoes():
                self.modo_edicao = False
                self.toggle_campos_edicao(False)
                self.ui.pushButton_2.setText("✏️ Editar")
        else:
            self.modo_edicao = True
            self.toggle_campos_edicao(True)
            self.ui.pushButton_2.setText("💾 Salvar")
    
    def toggle_campos_edicao(self, habilitar):
        self.ui.lineEdit.setEnabled(habilitar)
        self.ui.lineEdit_2.setEnabled(habilitar)
        self.ui.comboBox.setEnabled(habilitar)
        self.ui.comboBox_2.setEnabled(habilitar)
    
    def salvar_alteracoes(self):
        nome = self.ui.lineEdit.text().strip()
        email = self.ui.lineEdit_2.text().strip()
        federacao = self.ui.comboBox.currentText().strip()
        titulo_fide = self.ui.comboBox_2.currentText().strip()
        
        if not nome:
            QMessageBox.warning(self, "Validação", "O nome é obrigatório!")
            return False
        
        if not email:
            QMessageBox.warning(self, "Validação", "O email é obrigatório!")
            return False
   
        if email != self.jogador_data.get('email', ''):
            try:
                email_existe = self.api_client.verificar_email_existente(
                    email, 
                    self.jogador_data['id']
                )
                
                if email_existe:
                    QMessageBox.warning(
                        self, 
                        "Email já cadastrado", 
                        "Este email já está cadastrado para outro jogador. Por favor, use outro email."
                    )
                    self.ui.lineEdit_2.selectAll()
                    self.ui.lineEdit_2.setFocus()
                    return False
                    
            except Exception as e:
                QMessageBox.warning(self, "Aviso", "Não foi possível verificar o email. Tente novamente.")
                return False
        
        try:
            dados_atualizacao = {
                'nome': nome,
                'email': email,
                'federacao': federacao if federacao != '' else None,
                'titulo_fide': titulo_fide if titulo_fide !='' else None 
            }
            
            jogador_atualizado = self.api_client.atualizar_jogador(
                self.jogador_data['id'], 
                dados_atualizacao
            )
            
            self.jogador_data.update(dados_atualizacao)
            
            QMessageBox.information(self, "Sucesso", "Jogador atualizado com sucesso!")
            return True
            
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao atualizar jogador: {str(e)}")
            return False
    
    def excluir_jogador(self):
        resposta = QMessageBox.question(
            self,
            "Confirmar Exclusão",
            f"Tem certeza que deseja excluir o jogador {self.jogador_data.get('nome', '')}?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        
        if resposta == QMessageBox.Yes:
            try:
                jogador_id = self.jogador_data.get('id')
                self.api_client.excluir_jogador(jogador_id)
                
                QMessageBox.information(self, "Sucesso", "Jogador excluído com sucesso!")

                self.jogador_data = None
                self.done(QDialog.Accepted)
                    
            except Exception as e:
                QMessageBox.critical(self, "Erro", f"Erro ao excluir jogador: {str(e)}")
    
    def fechar(self):
        if self.modo_edicao:
            resposta = QMessageBox.question(
                self,
                "Alterações não salvas",
                "Há alterações não salvas. Deseja salvar antes de fechar?",
                QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel,
                QMessageBox.Save
            )
            
            if resposta == QMessageBox.Save:
                if not self.salvar_alteracoes():
                    return
            elif resposta == QMessageBox.Cancel:
                return
        
        self.accept()
    
    def get_dados_atualizados(self):
        if self.jogador_data is None:
            return None
        return self.jogador_data