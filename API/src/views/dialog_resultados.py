from PySide6.QtWidgets import QDialog, QListWidgetItem
from dialog_visualizar_jogador import DialogVisualizarJogador
from dialog_visualizar_partida import DialogVisualizarPartida
from ui_dialog_resultados import Ui_Dialog

import sys
import os

src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(src_path)
from utils.Uteis import calcular_idade

class DialogResultados(QDialog):
    def __init__(self, parent=None, resultados=None, tipo="jogadores"):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.tipo = tipo
        self.ui.pushButton.setEnabled(False)
        self.ui.pushButton.clicked.connect(self.mostrar_detalhes)
        self.ui.pushButton_2.clicked.connect(self.fechar)
        self.ui.listWidget.itemSelectionChanged.connect(self.verificar_selecao)
        self.setFixedSize(self.size())
        
        if tipo == "partidas":
            self.setWindowTitle("Resultados da Busca")
            self.ui.label.setText("Partidas Encontradas")

        else:
            self.setWindowTitle("Resultados da Busca")
            self.ui.label.setText("Jogadores Encontrados")

        if resultados:
            self.carregar_resultados(resultados)

    def verificar_selecao(self):
        tem_selecao = self.ui.listWidget.currentItem() is not None
        self.ui.pushButton.setEnabled(tem_selecao)
    
    def carregar_resultados(self, resultados):
        self.ui.listWidget.clear()
        
        if self.tipo == "jogadores":
            self.carregar_jogadores(resultados)
        else:
            self.carregar_partidas(resultados)
    
    def carregar_jogadores(self, jogadores):
        for jogador in jogadores:
            rating = jogador.get('rating')
            nome = jogador.get('nome')
            if jogador.get('federacao'):
                federacao = jogador.get('federacao')
            else: federacao = 'N/A'
            if jogador.get('titulo_fide'):
                titulo = jogador.get('titulo_fide')
            else: titulo = ''
            data_nascimento_str = jogador.get('data_nascimento')

            if data_nascimento_str:
                from datetime import datetime
                data_nasc = datetime.strptime(data_nascimento_str, '%Y-%m-%d').date()
                idade = calcular_idade(data_nasc)
            else:
                idade = "N/A"
            
            nome_completo = f"{titulo} {nome}".strip() if titulo else nome
            item_text = f"{rating} {nome_completo}\n{federacao}, {idade} anos"
            
            item = QListWidgetItem(item_text)
            item.setData(1000, jogador)
            self.ui.listWidget.addItem(item)
    
    def carregar_partidas(self, partidas):
        for partida in partidas:
            brancas = partida.get('jogador_brancas')
            pretas = partida.get('jogador_pretas')
            resultado = partida.get('resultado')
            data = partida.get('data_partida')
            evento = partida.get('evento')
      
            if data != 'N/A':
                try:
                    from datetime import datetime
                    data_obj = datetime.strptime(data, '%a, %d %b %Y %H:%M:%S GMT')
                    data = data_obj.strftime('%d/%m/%Y')
                except:
                    pass  
            
            item_text = f"{brancas} vs {pretas}\n{resultado} - {data} - {evento}"
            
            item = QListWidgetItem(item_text)
            item.setData(1000, partida)
            self.ui.listWidget.addItem(item)
            
    def mostrar_detalhes(self):
        item_selecionado = self.ui.listWidget.currentItem()
        
        if not item_selecionado:
            from PySide6.QtWidgets import QMessageBox
            QMessageBox.warning(self, "Aviso", "Selecione um item para ver os detalhes!")
            return
        
        dados = item_selecionado.data(1000)
        
        if self.tipo == "jogadores":
            self.mostrar_detalhes_jogador(dados)
        else:
            self.mostrar_detalhes_partida(dados)
    
    def mostrar_detalhes_jogador(self, jogador):
        dialog = DialogVisualizarJogador(self, jogador)
        result = dialog.exec()
        
        if result == QDialog.Accepted:
            dados_atualizados = dialog.get_dados_atualizados()
            if dados_atualizados:
                self.atualizar_item_lista(dados_atualizados)
            else:
                self.remover_item_lista(jogador['id'])

    def remover_item_lista(self, jogador_id):
        for i in range(self.ui.listWidget.count()):
            item = self.ui.listWidget.item(i)
            dados = item.data(1000)
            
            if dados.get('id') == jogador_id:
                self.ui.listWidget.takeItem(i)
                break

    def atualizar_item_lista(self, jogador_atualizado):
        for i in range(self.ui.listWidget.count()):
            item = self.ui.listWidget.item(i)
            dados = item.data(1000)
            
            if dados.get('id') == jogador_atualizado.get('id'):
                item.setData(1000, jogador_atualizado)
                
                rating = dados.get('rating')
                nome = jogador_atualizado.get('nome')
                federacao = jogador_atualizado.get('federacao') or 'N/A'
                titulo = jogador_atualizado.get('titulo_fide') or ''

                data_nascimento_str = jogador_atualizado.get('data_nascimento')
                if data_nascimento_str:
                    from datetime import datetime
                    data_nasc = datetime.strptime(data_nascimento_str, '%Y-%m-%d').date()
                    idade = calcular_idade(data_nasc)
                else:
                    idade = "N/A"
                
                nome_completo = f"{titulo} {nome}".strip() if titulo else nome
                item_text = f"{rating} {nome_completo}\n{federacao}, {idade} anos"
                
                item.setText(item_text)
                break
    
    def mostrar_detalhes_partida(self, partida):
      
        try:
          
            if 'lances' not in partida or 'controle_tempo' not in partida:
            
                from APIClient import APIClient
                api_client = APIClient()
                partida_completa = api_client.buscar_partida(partida['id'])
            else:
                partida_completa = partida
            
            dialog = DialogVisualizarPartida(self, partida_id=partida_completa['id'])
            result = dialog.exec()
            
            if result == QDialog.Accepted:
            
                self.remover_partida_lista(partida['id'])
                
        except Exception as e:
            from PySide6.QtWidgets import QMessageBox
            QMessageBox.critical(self, "Erro", f"Erro ao carregar partida: {str(e)}")

    def remover_partida_lista(self, partida_id):
   
        for i in range(self.ui.listWidget.count()):
            item = self.ui.listWidget.item(i)
            dados = item.data(1000)
            
            if dados.get('id') == partida_id:
                self.ui.listWidget.takeItem(i)
                break
        
    def get_item_selecionado(self):
        item_selecionado = self.ui.listWidget.currentItem()
        if item_selecionado:
            return item_selecionado.data(1000)
        return None
    
    def fechar(self):
        self.reject()