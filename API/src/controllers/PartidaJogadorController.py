import re
from flask_restful import Resource, abort, request
from flask_apispec import marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from marshmallow import Schema, ValidationError, fields, validates
from sqlalchemy.exc import IntegrityError, OperationalError
from src.repositories.PartidaJogadorRepository import (
    adicionar_jogador_partida, 
    get_jogadores_partida, 
    get_partidas_jogador
)
from src.repositories.PartidaRepository import get_partida
from src.repositories.JogadorRepository import get_jogador

class PartidaJogadorResponseSchema(Schema):
    id = fields.Int()
    partida_id = fields.Int()
    jogador_id = fields.Int()
    cor = fields.Str()

class PartidaJogadorRequestSchema(Schema):
    partida_id = fields.Int(required=True)
    jogador_id = fields.Int(required=True)
    cor = fields.Str(required=True)
    
    @validates("cor")
    def validate_cor(self, value):
        if value not in ['brancas', 'pretas']:
            raise ValidationError("Cor deve ser 'brancas' ou 'pretas'")

class PartidaJogadorDetalhadoResponseSchema(Schema):
    id = fields.Int()
    partida_id = fields.Int()
    jogador_id = fields.Int()
    cor = fields.Str()
    jogador_nome = fields.Str()
    jogador_rating = fields.Int()
    partida_evento = fields.Str()
    partida_data = fields.Date()
    partida_resultado = fields.Str()

class CriarPartidaJogador(MethodResource, Resource):
    @use_kwargs(PartidaJogadorRequestSchema, location=("json"))
    @marshal_with(PartidaJogadorResponseSchema)
    def post(self, **kwargs):
    
        try:
            partida = get_partida(kwargs['partida_id'])
            if not partida:
                abort(404, message="Partida não encontrada")
            
            jogador = get_jogador(kwargs['jogador_id'])
            if not jogador:
                abort(404, message="Jogador não encontrado")
            
            partida_jogador = adicionar_jogador_partida(**kwargs)
            return partida_jogador, 201
        except IntegrityError as err:
            error_msg = str(err.orig)
            if "partida_jogador_partida_id_cor_key" in error_msg:
                abort(400, message=f"Já existe um jogador com as {kwargs['cor']} nesta partida")
            elif "partida_jogador_partida_id_jogador_id_key" in error_msg:
                abort(400, message="Este jogador já está cadastrado nesta partida")
            else:
                abort(500, message="Erro de integridade nos dados")
        except OperationalError as err:
            abort(500, message=str(err.__context__))

class JogadoresPartidaList(MethodResource, Resource):
    @marshal_with(PartidaJogadorDetalhadoResponseSchema(many=True))
    def get(self, partida_id):
       
        try:
            from src.entities.PartidaJogador import PartidaJogador
            from src.entities.Jogador import Jogador
            from src.entities.Partida import Partida
            from src.entities.database import db
            
            jogadores_partida = (db.session.query(
                PartidaJogador,
                Jogador.nome.label('jogador_nome'),
                Jogador.rating.label('jogador_rating'),
                Partida.evento.label('partida_evento'),
                Partida.data_partida.label('partida_data'),
                Partida.resultado.label('partida_resultado')
            )
            .join(Jogador, PartidaJogador.jogador_id == Jogador.id)
            .join(Partida, PartidaJogador.partida_id == Partida.id)
            .filter(PartidaJogador.partida_id == partida_id)
            .all())
            
            result = []
            for pj, jogador_nome, jogador_rating, partida_evento, partida_data, partida_resultado in jogadores_partida:
                result.append({
                    'id': pj.id,
                    'partida_id': pj.partida_id,
                    'jogador_id': pj.jogador_id,
                    'cor': pj.cor,
                    'jogador_nome': jogador_nome,
                    'jogador_rating': jogador_rating,
                    'partida_evento': partida_evento,
                    'partida_data': partida_data,
                    'partida_resultado': partida_resultado
                })
            
            return result, 200
        except OperationalError:
            abort(500, message="Erro interno do servidor")

class PartidasJogadorList(MethodResource, Resource):
    @marshal_with(PartidaJogadorDetalhadoResponseSchema(many=True))
    def get(self, jogador_id):
       
        try:
            from src.entities.PartidaJogador import PartidaJogador
            from src.entities.Jogador import Jogador
            from src.entities.Partida import Partida
            from src.entities.database import db
            
            partidas_jogador = (db.session.query(
                PartidaJogador,
                Jogador.nome.label('jogador_nome'),
                Jogador.rating.label('jogador_rating'),
                Partida.evento.label('partida_evento'),
                Partida.data_partida.label('partida_data'),
                Partida.resultado.label('partida_resultado')
            )
            .join(Jogador, PartidaJogador.jogador_id == Jogador.id)
            .join(Partida, PartidaJogador.partida_id == Partida.id)
            .filter(PartidaJogador.jogador_id == jogador_id)
            .all())
            
            result = []
            for pj, jogador_nome, jogador_rating, partida_evento, partida_data, partida_resultado in partidas_jogador:
                result.append({
                    'id': pj.id,
                    'partida_id': pj.partida_id,
                    'jogador_id': pj.jogador_id,
                    'cor': pj.cor,
                    'jogador_nome': jogador_nome,
                    'jogador_rating': jogador_rating,
                    'partida_evento': partida_evento,
                    'partida_data': partida_data,
                    'partida_resultado': partida_resultado
                })
            
            return result, 200
        except OperationalError:
            abort(500, message="Erro interno do servidor")