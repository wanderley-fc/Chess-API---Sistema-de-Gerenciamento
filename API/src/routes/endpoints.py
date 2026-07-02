from src.controllers.JogadorController import JogadorList, JogadorItem, JogadorBuscar
from src.controllers.PartidaController import PartidaList, PartidaItem, PartidaBuscar
from src.controllers.JogadorController import JogadorVerificarEmail, JogadorEstatisticas
from src.controllers.PartidaJogadorController import (
    CriarPartidaJogador, 
    JogadoresPartidaList, 
    PartidasJogadorList
)


def initialize_endpoints(api):

    api.add_resource(JogadorList, "/jogadores")
    api.add_resource(JogadorItem, "/jogador/<int:jogador_id>")

    api.add_resource(PartidaList, "/partidas")
    api.add_resource(PartidaItem, "/partida/<int:partida_id>")
    api.add_resource(PartidaBuscar, "/partidas/buscar")

    api.add_resource(CriarPartidaJogador, '/partida_jogadores')
    api.add_resource(JogadoresPartidaList, '/partida/<int:partida_id>/jogadores')
    api.add_resource(PartidasJogadorList, '/jogador/<int:jogador_id>/partidas')
    api.add_resource(JogadorBuscar, '/jogadores/buscar')
    api.add_resource(JogadorVerificarEmail, '/jogadores/verificar-email')
    api.add_resource(JogadorEstatisticas, '/jogador/<int:jogador_id>/estatisticas')
    