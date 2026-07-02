import requests
from typing import List, Dict, Optional

class APIClient:
    def __init__(self, base_url: str = "http://localhost:5000/xadrez"):
        self.base_url = base_url
    
    def buscar_jogadores(self, filtros: Dict) -> List[Dict]:
        try:
            params = {k: v for k, v in filtros.items() if v}
            
            response = requests.get(
                f"{self.base_url}/jogadores/buscar", 
                params=params,
                timeout=10
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.ConnectionError:
            raise Exception("Não foi possível conectar à API. Verifique se o servidor está rodando.")
        except requests.exceptions.Timeout:
            raise Exception("Tempo de conexão esgotado.")
        except requests.exceptions.RequestException as e:
            raise Exception(f"Erro na requisição: {str(e)}")
    
    def testar_conexao(self) -> bool:
        try:
            response = requests.get(f"{self.base_url}/jogadores", timeout=5)
            return response.status_code == 200
        except:
            return False
        
    def cadastrar_jogador(self, dados_jogador: Dict) -> Optional[Dict]:
        try:
            response = requests.post(
                f"{self.base_url}/jogadores",
                json=dados_jogador,
                timeout=10
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            if hasattr(e, 'response') and e.response is not None:
                error_message = f"Erro {e.response.status_code}"
                if 'application/json' in e.response.headers.get('content-type', ''):
                    try:
                        error_data = e.response.json()
                        error_message = error_data.get('message', str(error_data))
                    except:
                        error_message = e.response.text
                else:
                    if "Email já cadastrado" in e.response.text:
                        error_message = "Email já cadastrado"
                    elif "Unprocessable Entity" in e.response.text:
                        error_message = "Erro de validação nos dados enviados"
                
                if e.response.status_code == 422:
                    raise Exception(f"Erro de validação: {error_message}")
                else:
                    raise Exception(f"Erro {e.response.status_code}: {error_message}")
            else:
                raise Exception(f"Erro de conexão: {str(e)}")

    def excluir_jogador(self, jogador_id: int) -> bool:
        try:
            response = requests.delete(f"{self.base_url}/jogador/{jogador_id}")
            response.raise_for_status()
            return True
        except requests.exceptions.RequestException as e:
            raise Exception(f"Erro ao excluir jogador: {str(e)}")
        
    def atualizar_jogador(self, jogador_id: int, dados_jogador: Dict) -> Optional[Dict]:
        try:
            response = requests.put(
                f"{self.base_url}/jogador/{jogador_id}",
                json=dados_jogador,
                timeout=10
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            if e.response.status_code == 400:
                error_msg = e.response.json().get('message', 'Dados inválidos')
                raise Exception(f"Erro de validação: {error_msg}")
            else:
                raise Exception(f"Erro ao atualizar jogador: {str(e)}")
            
    def verificar_email_existente(self, email: str, excluir_jogador_id: int = None) -> bool:
        try:
            params = {'email': email}
            if excluir_jogador_id is not None:
                params['excluir_id'] = excluir_jogador_id
                
            response = requests.get(f"{self.base_url}/jogadores/verificar-email", params=params)
            response.raise_for_status()
            return response.json().get('existe', False)
        except requests.exceptions.RequestException:
            return False
        
    def buscar_partidas(self) -> List[Dict]:
      
        try:
            response = requests.get(f"{self.base_url}/partidas", timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Erro ao buscar partidas: {str(e)}")

    def buscar_partida(self, partida_id: int) -> Optional[Dict]:
      
        try:
            response = requests.get(f"{self.base_url}/partida/{partida_id}", timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            if e.response.status_code == 404:
                raise Exception("Partida não encontrada")
            else:
                raise Exception(f"Erro ao buscar partida: {str(e)}")
            
    def buscar_partidas_com_filtros(self, filtros: Dict) -> List[Dict]:
        try:
            params = {k: v for k, v in filtros.items() if v is not None and v != ""}
            
            response = requests.get(
                f"{self.base_url}/partidas/buscar", 
                params=params,
                timeout=10
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.ConnectionError:
            raise Exception("Não foi possível conectar à API. Verifique se o servidor está rodando.")
        except requests.exceptions.Timeout:
            raise Exception("Tempo de conexão esgotado.")
        except requests.exceptions.RequestException as e:
            if e.response.status_code == 400:
                error_msg = e.response.json().get('message', 'Dados inválidos')
                raise Exception(f"Erro de validação: {error_msg}")
            else:
                raise Exception(f"Erro na busca de partidas: {str(e)}")

    def excluir_partida(self, partida_id: int) -> bool:
        try:
            response = requests.delete(f"{self.base_url}/partida/{partida_id}")
            response.raise_for_status()
            return True
        except requests.exceptions.RequestException as e:
            if e.response.status_code == 404:
                raise Exception("Partida não encontrada")
            else:
                raise Exception(f"Erro ao excluir partida: {str(e)}")
            
    def cadastrar_partida(self, dados_partida: Dict) -> Optional[Dict]:
        try:
            response = requests.post(
                f"{self.base_url}/partidas",
                json=dados_partida,
                timeout=10
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            if e.response.status_code == 400:
                error_msg = e.response.json().get('message', 'Dados inválidos')
                raise Exception(f"Erro de validação: {error_msg}")
            else:
                raise Exception(f"Erro ao cadastrar partida: {str(e)}")
            
    def get_estatisticas(self, jogador_id: int) -> Optional[Dict]:
        try:
            response = requests.get(
                f"{self.base_url}/jogador/{jogador_id}/estatisticas",
                timeout=10
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            if e.response and e.response.status_code == 404:
                raise Exception("Estatísticas do jogador não encontradas")
            else:
                raise Exception(f"Erro ao buscar estatísticas: {str(e)}")