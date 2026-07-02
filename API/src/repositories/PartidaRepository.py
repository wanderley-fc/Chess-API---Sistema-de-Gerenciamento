from src.entities.Partida import Partida
from src.entities.database import db

def get_lista_partidas():
   
    partidas = db.session.query(Partida).order_by(Partida.data_partida.desc()).all()
    
    return partidas

def get_partida(partida_id):
  
    partida = db.session.query(Partida).get(partida_id)
    
    return partida

def get_partida_com_jogadores(partida_id):

    from src.repositories.PartidaJogadorRepository import get_jogadores_partida_com_nomes
    
    partida = db.session.query(Partida).get(partida_id)
    if not partida:
        return None

    jogadores_partida = get_jogadores_partida_com_nomes(partida_id)

    jogador_brancas = "Anônimo"
    jogador_pretas = "Anônimo"
    
    for jogador_info in jogadores_partida:
        if jogador_info['cor'] == 'brancas':
            jogador_brancas = jogador_info['nome']
        elif jogador_info['cor'] == 'pretas':
            jogador_pretas = jogador_info['nome']
    
    partida_data = {
        'id': partida.id,
        'evento': partida.evento,
        'local_evento': partida.local_evento,
        'data_partida': partida.data_partida,  
        'resultado': partida.resultado,
        'terminacao': partida.terminacao,
        'controle_tempo': partida.controle_tempo,
        'rodada': partida.rodada,
        'lances': partida.lances,
        'jogador_brancas': jogador_brancas,
        'jogador_pretas': jogador_pretas,
        'jogadores_detalhes': jogadores_partida
    }
    
    return partida_data

def buscar_partidas_com_filtros(filtros: dict):
    from src.entities.PartidaJogador import PartidaJogador
    from src.entities.Jogador import Jogador
    
    query = db.session.query(Partida).distinct()

    if 'jogador_brancas' in filtros and filtros['jogador_brancas']:
        query = query.join(
            PartidaJogador, 
            (Partida.id == PartidaJogador.partida_id)
        ).join(
            Jogador, 
            PartidaJogador.jogador_id == Jogador.id
        ).filter(
            PartidaJogador.cor == 'brancas',
            Jogador.nome.ilike(f"%{filtros['jogador_brancas']}%")
        )
  
    if 'jogador_pretas' in filtros and filtros['jogador_pretas']:
        from sqlalchemy.orm import aliased

        PartidaJogadorPretas = aliased(PartidaJogador)
        JogadorPretas = aliased(Jogador)
        
        query = query.join(
            PartidaJogadorPretas, 
            Partida.id == PartidaJogadorPretas.partida_id
        ).join(
            JogadorPretas, 
            PartidaJogadorPretas.jogador_id == JogadorPretas.id
        ).filter(
            PartidaJogadorPretas.cor == 'pretas',
            JogadorPretas.nome.ilike(f"%{filtros['jogador_pretas']}%")
        )

    if 'resultado' in filtros and filtros['resultado']:
        query = query.filter(Partida.resultado == filtros['resultado'])

    if 'terminacao' in filtros and filtros['terminacao']:
        query = query.filter(Partida.terminacao == filtros['terminacao'])

    if 'ano' in filtros and filtros['ano']:
        from sqlalchemy import extract
        query = query.filter(extract('year', Partida.data_partida) == int(filtros['ano']))
    
    return query.order_by(Partida.data_partida.desc()).all()

def add_partida(evento: str = None, local_evento: str = None, data_partida = None, 
                resultado: str = None, terminacao: str = None, controle_tempo: str = None,
                rodada: str = None, lances: str = None):

    evento = evento if evento != "" else None
    local_evento = local_evento if local_evento != "" else None
    data_partida = data_partida if data_partida != "" else None 
    terminacao = terminacao if terminacao != "" else None
    controle_tempo = controle_tempo if controle_tempo != "" else None
    rodada = rodada if rodada != "" else None
    lances = lances if lances != "" else None

    partida = Partida(
        evento=evento,
        local_evento=local_evento,
        data_partida=data_partida,
        resultado=resultado,
        terminacao=terminacao,
        controle_tempo=controle_tempo,
        rodada=rodada,
        lances=lances
    )
    
    db.session.add(partida)
    db.session.commit()

    return partida

def update_partida(partida_id: int, **kwargs):
    
    partida = db.session.query(Partida).get(partida_id)

    if not partida:
        raise Exception("Partida não encontrada")
    
    for key, value in kwargs.items():
        if hasattr(partida, key):
            setattr(partida, key, value)

    db.session.commit()
    return partida

def delete_partida(partida_id):
    from src.entities.PartidaJogador import PartidaJogador
    
    partida = db.session.query(Partida).get(partida_id)
    if not partida:
        raise Exception("Partida não encontrada")
    
    db.session.query(PartidaJogador).filter(
        PartidaJogador.partida_id == partida_id
    ).delete()

    db.session.delete(partida)
    db.session.commit()
    
    return partida