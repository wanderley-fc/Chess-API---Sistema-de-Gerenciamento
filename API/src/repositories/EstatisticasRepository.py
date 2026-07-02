from src.entities.database import db
from src.entities.PartidaJogador import PartidaJogador
from src.entities.Partida import Partida

def get_estatisticas_jogador_sql(jogador_id: int):

    query = db.session.query(
        db.func.count(PartidaJogador.id).label('total_partidas'),
        db.func.sum(
            db.case(
                [
                    (
                        (Partida.resultado == '1-0') & (PartidaJogador.cor == 'brancas') |
                        (Partida.resultado == '0-1') & (PartidaJogador.cor == 'pretas'),
                        1
                    )
                ],
                else_=0
            )
        ).label('vitorias'),
        db.func.sum(
            db.case(
                [(Partida.resultado == '1/2-1/2', 1)],
                else_=0
            )
        ).label('empates'),
        db.func.sum(
            db.case(
                [
                    (
                        (Partida.resultado == '0-1') & (PartidaJogador.cor == 'brancas') |
                        (Partida.resultado == '1-0') & (PartidaJogador.cor == 'pretas'),
                        1
                    )
                ],
                else_=0
            )
        ).label('derrotas')
    ).join(
        Partida, PartidaJogador.partida_id == Partida.id
    ).filter(
        PartidaJogador.jogador_id == jogador_id,
        Partida.resultado.in_(['1-0', '0-1', '1/2-1/2'])  
    )
    
    result = query.first()
    
    if not result:
        return {
            'total_partidas': 0,
            'vitorias': 0,
            'empates': 0,
            'derrotas': 0
        }

    total_partidas = result.total_partidas or 0
    vitorias = result.vitorias or 0
    empates = result.empates or 0
    derrotas = result.derrotas or 0
    
    return {
        'total_partidas': total_partidas,
        'vitorias': vitorias,
        'empates': empates,
        'derrotas': derrotas
    }