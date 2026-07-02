from src.entities.PartidaJogador import PartidaJogador
from src.entities.database import db

def adicionar_jogador_partida(partida_id: int, jogador_id: int, cor: str):

    partida_jogador = PartidaJogador(
        partida_id=partida_id,
        jogador_id=jogador_id,
        cor=cor
    )
    
    db.session.add(partida_jogador)
    db.session.commit()

    return partida_jogador

def get_jogadores_partida(partida_id):
    
    jogadores = db.session.query(PartidaJogador).filter(
        PartidaJogador.partida_id == partida_id
    ).all()
    
    return jogadores

def get_jogadores_partida_com_nomes(partida_id):
    
    from src.entities.Jogador import Jogador
    
    jogadores_partida = db.session.query(PartidaJogador, Jogador).join(
        Jogador, PartidaJogador.jogador_id == Jogador.id
    ).filter(
        PartidaJogador.partida_id == partida_id
    ).all()
    
    resultado = []
    for pj, jogador in jogadores_partida:
        resultado.append({
            'partida_jogador_id': pj.id,
            'jogador_id': jogador.id,
            'nome': jogador.nome,
            'cor': pj.cor,
            'rating': jogador.rating
        })
    
    return resultado

def get_partidas_jogador(jogador_id):
    
    partidas = db.session.query(PartidaJogador).filter(
        PartidaJogador.jogador_id == jogador_id
    ).all()
    
    return partidas