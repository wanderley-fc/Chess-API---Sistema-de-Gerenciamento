from src.repositories.JogadorRepository import delete_jogador, update_jogador, add_jogador, get_lista_jogadores, get_jogador
from src.entities.Jogador import Jogador
from src.utils.Uteis import (
    validar_federacao, validar_titulo_fide, validar_nome, validar_email, 
    TITULOS_FIDE, calcular_idade, validar_rating, 
    RATING_MINIMO, RATING_MAXIMO, RATING_PADRAO  
)
from marshmallow import ValidationError
from datetime import date

def getJogadores():
   
    return get_lista_jogadores()

def buscarJogadores(filtros: dict):
    from src.repositories.JogadorRepository import buscar_jogadores_com_filtros

    if 'idade_min' in filtros and filtros['idade_min']:
        try:
            idade_min = int(filtros['idade_min'])

        except ValueError:
            raise ValidationError("Idade mínima deve ser um número válido.")

    if 'idade_max' in filtros and filtros['idade_max']:
        try:
            idade_max = int(filtros['idade_max'])
        except ValueError:
            raise ValidationError("Idade máxima deve ser um número válido.")

    if ('idade_min' in filtros and filtros['idade_min'] and 
        'idade_max' in filtros and filtros['idade_max']):
        if int(filtros['idade_min']) > int(filtros['idade_max']):
            raise ValidationError("Idade mínima não pode ser maior que idade máxima.")
    
    return buscar_jogadores_com_filtros(filtros)

def getJogador(jogador_id):
   
    return get_jogador(jogador_id)

def addJogador(nome: str, data_nascimento: date, email: str, federacao: str = None, rating: int = 1500, titulo_fide: str = None):
    
    if not validar_nome(nome):
        raise ValidationError("Nome deve conter apenas letras e espaços e não pode estar vazio.")
    
    if not data_nascimento:
        raise ValidationError("Data de nascimento é obrigatória.")
    
    if not validar_email(email):
        raise ValidationError("Email inválido.")
    
    idade = calcular_idade(data_nascimento)
    if idade < 5:
        raise ValidationError("Jogador deve ter pelo menos 5 anos de idade.")
    
    if rating is not None:
        if rating < 0:
            raise ValidationError("Rating não pode ser negativo.")
        if rating > 3000:
            raise ValidationError("Rating não pode ser superior a 3000.")

    if federacao and not validar_federacao(federacao):
        raise ValidationError(f"Federação '{federacao}' não é reconhecida pela FIDE.")
    
    if titulo_fide and not validar_titulo_fide(titulo_fide):
        raise ValidationError(f"Título FIDE '{titulo_fide}' inválido. Títulos válidos: {', '.join(TITULOS_FIDE)}")
    
    return add_jogador(
        nome=nome,
        data_nascimento=data_nascimento,
        email=email,
        federacao=federacao,
        rating=rating,
        titulo_fide=titulo_fide
    )

def updateJogador(jogador_id: int, **kwargs):
    from src.repositories.JogadorRepository import update_jogador, verificar_email_existente, get_jogador
    
    jogador_existente = get_jogador(jogador_id)
    if not jogador_existente:
        raise ValidationError("Jogador não encontrado")
    
    if 'nome' in kwargs and kwargs['nome']:
        if not validar_nome(kwargs['nome']):
            raise ValidationError("Nome deve conter apenas letras e espaços.")
    
    if 'email' in kwargs and kwargs['email']:
        if not validar_email(kwargs['email']):
            raise ValidationError("Email inválido.")

        if verificar_email_existente(kwargs['email'], jogador_id):
            raise ValidationError("Este email já está cadastrado para outro jogador.")
    
    if 'rating' in kwargs and kwargs['rating'] is not None:
        if kwargs['rating'] < 0:
            raise ValidationError("Rating não pode ser negativo.")
        if kwargs['rating'] > 3000:
            raise ValidationError("Rating não pode ser superior a 3000.")
    
    if 'federacao' in kwargs and kwargs['federacao']:
        if not validar_federacao(kwargs['federacao']):
            raise ValidationError(f"Federação '{kwargs['federacao']}' não é reconhecida pela FIDE.")
    
    if 'titulo_fide' in kwargs and kwargs['titulo_fide']:
        if not validar_titulo_fide(kwargs['titulo_fide']):
            raise ValidationError(f"Título FIDE '{kwargs['titulo_fide']}' inválido. Títulos válidos: {', '.join(TITULOS_FIDE)}")
    
    return update_jogador(jogador_id, **kwargs)

def deleteJogador(jogador_id):
    
    return delete_jogador(jogador_id)

def atualizar_rating_jogador(jogador_id: int, variacao_rating: int):
    from src.repositories.JogadorRepository import update_jogador, get_jogador
    
    jogador = get_jogador(jogador_id)
    if not jogador:
        raise ValidationError("Jogador não encontrado")

    rating_atual = jogador.rating or RATING_PADRAO
    novo_rating = rating_atual + variacao_rating

    if not validar_rating(novo_rating):
        return jogador

    return update_jogador(jogador_id, rating=novo_rating)

def get_estatisticas_jogador(jogador_id: int):
  
    try:
        from src.repositories.EstatisticasRepository import get_estatisticas_jogador_sql
        return get_estatisticas_jogador_sql(jogador_id)
    except Exception:

        from src.repositories.PartidaJogadorRepository import get_partidas_jogador
        from src.repositories.PartidaRepository import get_partida
        
        partidas_jogador = get_partidas_jogador(jogador_id)
        
        total_partidas = len(partidas_jogador)
        vitorias = 0
        empates = 0
        derrotas = 0
        
        for partida_jogador in partidas_jogador:
            partida = get_partida(partida_jogador.partida_id)
            if not partida or not partida.resultado:
                continue
                
            resultado = partida.resultado
            cor_jogador = partida_jogador.cor
            
            if resultado == '1-0':
                if cor_jogador == 'brancas':
                    vitorias += 1
                else:
                    derrotas += 1
            elif resultado == '0-1':
                if cor_jogador == 'pretas':
                    vitorias += 1
                else:
                    derrotas += 1
            elif resultado == '1/2-1/2':
                empates += 1
        
        return {
            'total_partidas': total_partidas,
            'vitorias': vitorias,
            'empates': empates,
            'derrotas': derrotas
        }
    
def deleteJogador(jogador_id):
   
    from src.repositories.JogadorRepository import delete_jogador_completo
    
    return delete_jogador_completo(jogador_id)