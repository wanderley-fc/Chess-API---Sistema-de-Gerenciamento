from flask_restful import Resource, abort, request
from flask_apispec import marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from marshmallow import Schema, ValidationError, fields, validates
from sqlalchemy.exc import IntegrityError, OperationalError
from src.services.PartidaService import (
    buscarPartidas, 
    addPartidaComNomes  
)
from src.repositories.PartidaRepository import (
    get_lista_partidas, get_partida, add_partida, update_partida, delete_partida, get_partida_com_jogadores
)

class PartidaResponseSchema(Schema):
    id = fields.Int()
    evento = fields.Str()
    local_evento = fields.Str()
    data_partida = fields.Date(format='%Y-%m-%d')
    resultado = fields.Str()
    terminacao = fields.Str()
    controle_tempo = fields.Str()
    rodada = fields.Str()
    lances = fields.Str()
    jogador_brancas = fields.Str()  
    jogador_pretas = fields.Str()   

class PartidaRequestSchema(Schema):
    evento = fields.Str(allow_none=True)           
    local_evento = fields.Str(allow_none=True)       
    data_partida = fields.Date(format='%Y-%m-%d', allow_none=True)   
    resultado = fields.Str(allow_none=True)        
    terminacao = fields.Str(allow_none=True)       
    controle_tempo = fields.Str(allow_none=True)   
    rodada = fields.Str(allow_none=True)           
    lances = fields.Str(allow_none=True)   
    
    @validates("resultado")
    def validate_resultado(self, value):
        if value and value not in ['1-0', '0-1', '1/2-1/2', '*']:
            raise ValidationError("Resultado deve ser: '1-0', '0-1', '1/2-1/2' ou '*'")
    
    @validates("terminacao")
    def validate_terminacao(self, value):
        terminacoes_validas = [
            'Abandono', 'Afogamento', 'Xeque-mate', 'Empate por acordo', 
            'Empate por repetição', 'Empate por insuficiencia material', 
            'Empate por regra dos 50 lances', 'Timeout', 'Vitória por tempo'
        ]
        if value and value not in terminacoes_validas:
            raise ValidationError(f"Terminação deve ser uma das opções: {', '.join(terminacoes_validas)}")
        
class PartidaCreateRequestSchema(Schema):
    evento = fields.Str(allow_none=True)           
    local_evento = fields.Str(allow_none=True)       
    data_partida = fields.Date(format='%Y-%m-%d', allow_none=True) 
    resultado = fields.Str(allow_none=True)        
    terminacao = fields.Str(allow_none=True)       
    controle_tempo = fields.Str(allow_none=True)   
    rodada = fields.Str(allow_none=True)           
    lances = fields.Str(allow_none=True)
    jogador_brancas = fields.Str(allow_none=True)  
    jogador_pretas = fields.Str(allow_none=True)   
    
    @validates("resultado")
    def validate_resultado(self, value):
        if value and value not in ['1-0', '0-1', '1/2-1/2', '*']:
            raise ValidationError("Resultado deve ser: '1-0', '0-1', '1/2-1/2' ou '*'")
    
    @validates("terminacao")
    def validate_terminacao(self, value):
        terminacoes_validas = [
            'Abandono', 'Afogamento', 'Xeque-mate', 'Empate por acordo', 
            'Empate por repetição', 'Empate por insuficiencia material', 
            'Empate por regra dos 50 lances', 'Timeout', 'Vitória por tempo'
        ]
        if value and value not in terminacoes_validas:
            raise ValidationError(f"Terminação deve ser uma das opções: {', '.join(terminacoes_validas)}")

class PartidaItem(MethodResource, Resource):
    @marshal_with(PartidaResponseSchema)
    def get(self, partida_id):
        try:
            partida_data = get_partida_com_jogadores(partida_id)
            if not partida_data:
                abort(404, message="Partida não encontrada")
            return partida_data, 200
        except OperationalError:
            abort(500, message="Erro interno do servidor")

    @use_kwargs(PartidaRequestSchema, location=("json"))
    @marshal_with(PartidaResponseSchema)
    def put(self, partida_id, **kwargs):
        try:
            partida = update_partida(partida_id, **kwargs)
            return partida, 200
        except Exception as err:
            abort(500, message=str(err))
        except OperationalError as err:
            abort(500, message=str(err.__context__))

    def delete(self, partida_id):
        try:
            delete_partida(partida_id)
            return '', 204
        except Exception as err:
            abort(404, message="Partida não encontrada")
        except OperationalError:
            abort(500, message="Erro interno do servidor")

class PartidaList(MethodResource, Resource):
    @marshal_with(PartidaResponseSchema(many=True))
    def get(self):
        try:
            partidas = get_lista_partidas()
            partidas_basicas = []
            for partida in partidas:
                partidas_basicas.append({
                    'id': partida.id,
                    'evento': partida.evento,
                    'local_evento': partida.local_evento,
                    'data_partida': partida.data_partida,
                    'resultado': partida.resultado,
                    'terminacao': partida.terminacao,
                    'controle_tempo': partida.controle_tempo,
                    'rodada': partida.rodada,
                    'lances': partida.lances,
                    'jogador_brancas': 'A carregar...',  #
                    'jogador_pretas': 'A carregar...'    
                })
            return partidas_basicas, 200
        except OperationalError:
            abort(500, message="Erro interno do servidor")

    @use_kwargs(PartidaCreateRequestSchema, location=("json"))
    @marshal_with(PartidaResponseSchema)
    def post(self, **kwargs):
        try:
            from src.services.PartidaService import addPartidaComNomes  
            
            partida = addPartidaComNomes(**kwargs)
            return partida, 201
            
        except ValidationError as e:
            abort(400, message=str(e))
        except IntegrityError as err:
            abort(500, message="Erro de integridade nos dados")
        except OperationalError as err:
            abort(500, message=str(err.__context__))

class PartidaBuscar(MethodResource, Resource):
    def get(self):

        try:
            
            filtros = {
                'jogador_brancas': request.args.get('jogador_brancas'),
                'jogador_pretas': request.args.get('jogador_pretas'),
                'resultado': request.args.get('resultado'),
                'terminacao': request.args.get('terminacao'),
                'ano': request.args.get('ano')
            }
            
            partidas = buscarPartidas(filtros) 
            return partidas, 200
            
        except ValidationError as e:
            return {'message': str(e)}, 400
        except Exception as e:
            return {'message': f'Erro ao buscar partidas: {str(e)}'}, 500