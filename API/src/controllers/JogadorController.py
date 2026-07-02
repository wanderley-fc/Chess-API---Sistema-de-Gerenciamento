import re
from flask_restful import Resource, abort, request
from flask_apispec import marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from marshmallow import Schema, ValidationError, fields, validates
from sqlalchemy.exc import IntegrityError, OperationalError
from src.repositories.JogadorRepository import get_lista_jogadores, get_jogador, add_jogador, update_jogador, delete_jogador

class JogadorResponseSchema(Schema):
    id = fields.Int()
    nome = fields.Str()
    federacao = fields.Str()
    rating = fields.Int()
    data_nascimento = fields.Date()
    titulo_fide = fields.Str()
    email = fields.Str()
    data_cadastro = fields.Date()

class JogadorRequestSchema(Schema):
    nome = fields.Str(required=True)
    data_nascimento = fields.Date(format='%Y-%m-%d', required=True) 
    email = fields.Str(required=True)
    federacao = fields.Str(allow_none=True)
    rating = fields.Int(allow_none=True)
    titulo_fide = fields.Str(allow_none=True)
    

class JogadorUpdateSchema(Schema):
    nome = fields.Str(required=False, allow_none=True)  
    email = fields.Str(required=False, allow_none=True)
    data_nascimento = fields.Date(required=False, allow_none=True)
    federacao = fields.Str(required=False, allow_none=True)  
    rating = fields.Int(required=False, allow_none=True)
    titulo_fide = fields.Str(required=False, allow_none=True)

class JogadorEstatisticasSchema(Schema):
    total_partidas = fields.Int()
    vitorias = fields.Int()
    empates = fields.Int()
    derrotas = fields.Int()
    porcentagem_vitorias = fields.Float()
    porcentagem_empates = fields.Float()
    porcentagem_derrotas = fields.Float()

class JogadorBuscar(MethodResource, Resource):
    @marshal_with(JogadorResponseSchema(many=True))
    def get(self):
        try:
            from src.services.JogadorService import buscarJogadores
       
            filtros = {
                'nome': request.args.get('nome', ''),
                'email': request.args.get('email', ''),
                'titulo_fide': request.args.get('titulo_fide', ''),
                'federacao': request.args.get('federacao', ''),
                'idade_min': request.args.get('idade_min', ''),
                'idade_max': request.args.get('idade_max', '')
            }

            filtros = {k: v for k, v in filtros.items() if v}
            
            jogadores = buscarJogadores(filtros)
            return jogadores, 200
            
        except ValidationError as err:
            abort(400, message=err.messages)
        except Exception as err:
            abort(500, message=str(err))

class JogadorItem(MethodResource, Resource):
    @marshal_with(JogadorResponseSchema)
    def get(self, jogador_id):
        try:
            jogador = get_jogador(jogador_id)
            if not jogador:
                abort(404, message="Jogador não encontrado")
            return jogador, 200
        except OperationalError:
            abort(500, message="Erro interno do servidor")

    @use_kwargs(JogadorUpdateSchema, location=("json"))  
    @marshal_with(JogadorResponseSchema)
    def put(self, jogador_id, **kwargs):
        try:
            jogador = update_jogador(jogador_id, **kwargs)
            return jogador, 200
        except Exception as err:
            abort(500, message=str(err))
        except OperationalError as err:
            abort(500, message=str(err.__context__))

    def delete(self, jogador_id):
        try:
            from src.services.JogadorService import deleteJogador
            deleteJogador(jogador_id)
            return '', 204
        except Exception as err:
            abort(404, message="Jogador não encontrado")
        except OperationalError:
            abort(500, message="Erro interno do servidor")

class JogadorList(MethodResource, Resource):
    @marshal_with(JogadorResponseSchema(many=True))
    def get(self):
        try:
            return get_lista_jogadores(), 200
        except OperationalError:
            abort(500, message="Erro interno do servidor")

    @use_kwargs(JogadorRequestSchema, location=("json"))
    @marshal_with(JogadorResponseSchema)
    def post(self, **kwargs):
        try:
            print("=" * 50)
            print("DADOS RECEBIDOS NA API:")
            for key, value in kwargs.items():
                print(f"  {key}: {value} (tipo: {type(value)})")
            print("=" * 50)
            
            from src.services.JogadorService import addJogador  
            
            jogador = addJogador(**kwargs)  
            return jogador, 201
        except ValidationError as err:  
            print("ERRO DE VALIDAÇÃO NO SCHEMA:", err.messages)
            abort(422, message=err.messages)  
        except IntegrityError as err:
            print("ERRO DE INTEGRIDADE:", str(err))
            abort(500, message="Email já cadastrado")
        except Exception as err:
            print("ERRO INESPERADO:", str(err))
            abort(500, message=str(err))

class JogadorVerificarEmail(MethodResource, Resource):
    def get(self):
        try:
            from src.repositories.JogadorRepository import verificar_email_existente
            
            email = request.args.get('email', '')
            excluir_id = request.args.get('excluir_id', type=int)
            
            if not email:
                return {'existe': False}, 200
            
            existe = verificar_email_existente(email, excluir_id)
            return {'existe': existe}, 200
            
        except Exception as err:
            return {'existe': False}, 200
        
class JogadorEstatisticas(MethodResource, Resource):
    @marshal_with(JogadorEstatisticasSchema)
    def get(self, jogador_id):
        try:
            from src.services.JogadorService import get_estatisticas_jogador

            estatisticas = get_estatisticas_jogador(jogador_id)
   
            total = estatisticas['total_partidas']
            if total > 0:
                estatisticas['porcentagem_vitorias'] = (estatisticas['vitorias'] / total) * 100
                estatisticas['porcentagem_empates'] = (estatisticas['empates'] / total) * 100
                estatisticas['porcentagem_derrotas'] = (estatisticas['derrotas'] / total) * 100
            else:
                estatisticas['porcentagem_vitorias'] = 0
                estatisticas['porcentagem_empates'] = 0
                estatisticas['porcentagem_derrotas'] = 0
            
            return estatisticas, 200
            
        except Exception as err:
            abort(500, message=f"Erro ao buscar estatísticas: {str(err)}")