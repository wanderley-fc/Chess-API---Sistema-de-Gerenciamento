import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from PySide6.QtCore import QStringListModel  


src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(src_path)

from ui_form import Ui_MainFrame
from dialog_buscar_jogador import DialogBuscarJogador 
from dialog_cadastrar_partida import DialogCadastrarPartida 
from dialog_buscar_partida import DialogBuscarPartida
from dialog_cadastrar_jogador import DialogCadastrarJogador
from APIClient import APIClient

class MainFrame(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainFrame()
        self.ui.setupUi(self)
        self.api_client = APIClient()

        font = self.ui.listView.font()
        font.setPointSize(11)
        self.ui.listView.setFont(font)
        
        self.ui.pushButton.clicked.connect(self.abrir_janela_cadastrar_jogador)  
        self.ui.pushButton_2.clicked.connect(self.abrir_janela_buscar)
        self.ui.pushButton_3.clicked.connect(self.abrir_janela_cadastrar_partida)
        self.ui.pushButton_4.clicked.connect(self.abrir_janela_buscar_partida)

        self.setFixedSize(self.size())
        self.setWindowTitle("ChessAPI")
    
        self.model = QStringListModel()
        self.ui.listView.setModel(self.model)
        
        self.carregar_jogadores()
    
    def carregar_jogadores(self):

        try:
          
            jogadores = self.api_client.buscar_jogadores({})
            
            itens = []
            for jogador in jogadores:
                rating = jogador.get('rating') or 'N/A'
                nome = jogador.get('nome') or 'N/A'
                federacao = jogador.get('federacao') or 'N/A'
                titulo = jogador.get('titulo_fide') or ''
                
                nome_completo = f"{titulo} {nome}".strip() if titulo else nome
                item_text = f"{rating} {federacao} {nome_completo}"
                itens.append(item_text)
   
            self.model.setStringList(itens)
                
        except Exception as e:
            print(f"Erro ao carregar jogadores: {e}")
            self.model.setStringList(["Erro ao carregar jogadores. Verifique se a API está rodando."])
    
    def abrir_janela_cadastrar_jogador(self):
        dialog = DialogCadastrarJogador(self)
        dialog.exec()
        self.carregar_jogadores()
    
    def abrir_janela_buscar(self):
        dialog = DialogBuscarJogador(self)
        dialog.exec()
        self.carregar_jogadores()
       
    def abrir_janela_cadastrar_partida(self):
        dialog = DialogCadastrarPartida(self)
        dialog.exec()  
        self.carregar_jogadores()
    
    def abrir_janela_buscar_partida(self):
        dialog = DialogBuscarPartida(self)
        dialog.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainFrame()
    widget.show()
    sys.exit(app.exec())