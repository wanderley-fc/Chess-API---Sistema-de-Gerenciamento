from src.repositories.PartidaJogadorRepository import (
    adicionar_jogador_partida,
    get_jogadores_partida,
    get_partidas_jogador,
    get_jogadores_partida_com_nomes
)

def adicionarJogadorPartida(partida_id: int, jogador_id: int, cor: str):
    
    if cor not in ['brancas', 'pretas']:
        raise ValidationError("Cor deve ser 'brancas' ou 'pretas'")
    
    return adicionar_jogador_partida(partida_id, jogador_id, cor)

def getJogadoresPartida(partida_id: int):
    
    return get_jogadores_partida(partida_id)

def getJogadoresPartidaComNomes(partida_id: int):
   
    return get_jogadores_partida_com_nomes(partida_id)

def getPartidasJogador(jogador_id: int):
    
    return get_partidas_jogador(jogador_id)