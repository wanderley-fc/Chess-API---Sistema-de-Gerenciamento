from src.entities.Jogador import Jogador
from src.entities.database import db
from datetime import date
from sqlalchemy import or_, and_
from src.utils.Uteis import data_minima_por_idade, data_maxima_por_idade

def get_lista_jogadores():

    jogadores = db.session.query(Jogador).order_by(Jogador.rating.desc()).all()
    
    return jogadores

def get_jogador(jogador_id):

    jogador = db.session.query(Jogador).get(jogador_id)
    
    return jogador

def buscar_jogadores_com_filtros(filtros: dict):
    
    query = db.session.query(Jogador)
    
    if 'nome' in filtros and filtros['nome']:
        query = query.filter(Jogador.nome.ilike(f"%{filtros['nome']}%"))
    
    if 'email' in filtros and filtros['email']:
        query = query.filter(Jogador.email == filtros['email'])
    
    if 'titulo_fide' in filtros and filtros['titulo_fide']:
        query = query.filter(Jogador.titulo_fide == filtros['titulo_fide'])
    
    if 'federacao' in filtros and filtros['federacao']:
        query = query.filter(Jogador.federacao == filtros['federacao'])

    if 'idade_min' in filtros and filtros['idade_min']:
        idade_min = int(filtros['idade_min'])
        data_max_nascimento = data_minima_por_idade(idade_min)
        query = query.filter(Jogador.data_nascimento <= data_max_nascimento)

    if 'idade_max' in filtros and filtros['idade_max']:
        idade_max = int(filtros['idade_max'])
        data_min_nascimento = data_maxima_por_idade(idade_max)
        query = query.filter(Jogador.data_nascimento >= data_min_nascimento)

    query = query.order_by(Jogador.rating.desc().nulls_last())
    
    return query.all()

def add_jogador(nome: str, data_nascimento, email: str, federacao: str = None, rating: int = 1500, titulo_fide: str = None):
  
    if rating is None:
        rating = 1500  
    
    jogador = Jogador(
        nome=nome, 
        data_nascimento=data_nascimento, 
        email=email,
        federacao=federacao,
        rating=rating,  
        titulo_fide=titulo_fide
    )

    db.session.add(jogador)
    db.session.commit()
    db.session.refresh(jogador)
    
    return jogador

def update_jogador(jogador_id: int, **kwargs):
    
    jogador = db.session.query(Jogador).get(jogador_id)

    if not jogador:
        raise Exception("Jogador não encontrado")
    
    for key, value in kwargs.items():
        if hasattr(jogador, key):
            setattr(jogador, key, value)

    db.session.commit()
    return jogador

def delete_jogador(jogador_id):
   
    jogador = db.session.query(Jogador).get(jogador_id)
    db.session.delete(jogador)
    db.session.commit()
    return jogador

def verificar_email_existente(email: str, excluir_jogador_id: int = None) -> bool:
    
    query = db.session.query(Jogador).filter(Jogador.email == email)
    
    if excluir_jogador_id is not None:
        query = query.filter(Jogador.id != excluir_jogador_id)
    
    return query.first() is not None

def buscar_jogadores_por_nome(nome: str):
   
    if not nome:
        return []
    
    return db.session.query(Jogador).filter(
        Jogador.nome.ilike(f"%{nome}%")
    ).limit(10).all()

def delete_jogador_completo(jogador_id: int):
 
    from src.entities.PartidaJogador import PartidaJogador
    from src.entities.Partida import Partida
    
    try:

        db.session.begin()
        
        partidas_do_jogador = (db.session.query(PartidaJogador.partida_id)
                              .filter(PartidaJogador.jogador_id == jogador_id)
                              .all())
        
        partidas_ids = [p[0] for p in partidas_do_jogador]

        db.session.query(PartidaJogador).filter(
            PartidaJogador.jogador_id == jogador_id
        ).delete()

        for partida_id in partidas_ids:
            jogadores_restantes = db.session.query(PartidaJogador).filter(
                PartidaJogador.partida_id == partida_id
            ).count()

            if jogadores_restantes == 0:
                db.session.query(Partida).filter(
                    Partida.id == partida_id
                ).delete()

        jogador = db.session.query(Jogador).get(jogador_id)
        if jogador:
            db.session.delete(jogador)
  
        db.session.commit()
        return True
        
    except Exception as e:
        db.session.rollback()
        raise e