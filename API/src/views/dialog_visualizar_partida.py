from PySide6.QtWidgets import QDialog, QMessageBox
from ui_dialog_visualizar_partida import Ui_Dialog
from APIClient import APIClient

class DialogVisualizarPartida(QDialog):
    def __init__(self, parent=None, partida_id=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        self.partida_id = partida_id
        self.api_client = APIClient()
        self.partida_data = None
        self.setFixedSize(self.size())

        self.ui.btn_excluir.clicked.connect(self.excluir_partida)
        self.ui.btn_ok.clicked.connect(self.fechar)
   
        if partida_id:
            self.carregar_dados_partida()
    
    def carregar_dados_partida(self):
        
        try:
            self.partida_data = self.api_client.buscar_partida(self.partida_id)
            self.preencher_campos()
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao carregar partida: {str(e)}")
            self.reject()
    
    def preencher_campos(self):
        
        if not self.partida_data:
            return
        
        jogador_brancas = self.partida_data.get('jogador_brancas', 'N/A')
        jogador_pretas = self.partida_data.get('jogador_pretas', 'N/A')
        self.ui.label_jogadores.setText(f"{jogador_brancas} vs {jogador_pretas}")
        
        resultado = self.partida_data.get('resultado', 'N/A')
        self.ui.label_resultado.setText(f"Resultado: {resultado}")
        
        evento = self.partida_data.get('evento', 'N/A')
        local = self.partida_data.get('local_evento', 'N/A')
        self.ui.label_evento_local.setText(f"Evento: {evento} - Local: {local}")
        
        data_partida = self.partida_data.get('data_partida', 'N/A')
        self.ui.label_data.setText(f"Data: {data_partida}")
        
        terminacao = self.partida_data.get('terminacao', 'N/A')
        controle_tempo = self.partida_data.get('controle_tempo', 'N/A')
        rodada = self.partida_data.get('rodada', 'N/A')
        
        detalhes_text = f"Terminação: {terminacao}"
        if controle_tempo:
            detalhes_text += f" | Tempo: {controle_tempo}"
        if rodada:
            detalhes_text += f" | Rodada: {rodada}"
            
        self.ui.label_detalhes.setText(detalhes_text)
        
        lances = self.partida_data.get('lances', '')
        if lances:
            self.ui.textEdit_lances.setPlainText(lances)
        else:
            self.ui.textEdit_lances.setPlainText("Nenhuma sequência de lances registrada.")
    
    def excluir_partida(self):
      
        if not self.partida_data:
            return
        
        jogador_brancas = self.partida_data.get('jogador_brancas', '')
        jogador_pretas = self.partida_data.get('jogador_pretas', '')
        
        resposta = QMessageBox.question(
            self,
            "Confirmar Exclusão",
            f"Tem certeza que deseja excluir a partida:\n{jogador_brancas} vs {jogador_pretas}?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        
        if resposta == QMessageBox.Yes:
            try:
                self.api_client.excluir_partida(self.partida_id)
                QMessageBox.information(self, "Sucesso", "Partida excluída com sucesso!")
                self.accept()  
            except Exception as e:
                QMessageBox.critical(self, "Erro", f"Erro ao excluir partida: {str(e)}")
    
    def fechar(self):
        
        self.accept()
    
    def get_dados_partida(self):
        
        return self.partida_data