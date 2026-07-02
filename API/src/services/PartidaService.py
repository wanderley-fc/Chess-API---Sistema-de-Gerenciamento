from src.repositories.PartidaRepository import (
    delete_partida, update_partida, add_partida, get_lista_partidas, get_partida, get_partida_com_jogadores, buscar_partidas_com_filtros
)
from src.repositories.PartidaJogadorRepository import adicionar_jogador_partida
from src.repositories.JogadorRepository import get_jogador
from src.utils.Uteis import (
    validar_resultado, validar_terminacao, RESULTADOS_VALIDOS, TERMINACOES_VALIDAS
)
from marshmallow import ValidationError
from datetime import datetime

def getPartidas():
    return get_lista_partidas()

def buscarPartidas(filtros: dict):
    if 'ano' in filtros and filtros['ano']:
        try:
            ano = int(filtros['ano'])
            if ano < 1900 or ano > datetime.now().year + 1:
                raise ValidationError("Ano deve estar entre 1900 e o ano atual")
        except ValueError:
            raise ValidationError("Ano deve ser um número válido")

    if 'resultado' in filtros and filtros['resultado']:
        if not validar_resultado(filtros['resultado']):
            raise ValidationError(f"Resultado inválido. Resultados válidos: {', '.join(RESULTADOS_VALIDOS)}")

    if 'terminacao' in filtros and filtros['terminacao']:
        if not validar_terminacao(filtros['terminacao']):
            raise ValidationError(f"Terminação inválida. Terminações válidas: {', '.join(TERMINACOES_VALIDAS)}")
    
    partidas = buscar_partidas_com_filtros(filtros)
    
    partidas_com_jogadores = []
    for partida in partidas:
        partida_data = get_partida_com_jogadores(partida.id)
        partidas_com_jogadores.append(partida_data)
    
    return partidas_com_jogadores

def getPartida(partida_id):
    partida = get_partida(partida_id)
    if not partida:
        raise ValidationError("Partida não encontrada")
    return partida

def getPartidaComJogadores(partida_id):
    partida_data = get_partida_com_jogadores(partida_id)
    if not partida_data:
        raise ValidationError("Partida não encontrada")
    return partida_data

def addPartida(
    evento: str = None, 
    local_evento: str = None, 
    data_partida = None, 
    resultado: str = None, 
    terminacao: str = None, 
    controle_tempo: str = None,
    rodada: str = None, 
    lances: str = None,
    jogador_brancas_id: int = None,
    jogador_pretas_id: int = None
):
    if data_partida:
        try:
            if isinstance(data_partida, str):
                data_obj = datetime.strptime(data_partida, "%Y-%m-%d").date()
            else:
                data_obj = data_partida
                
            if data_obj > datetime.now().date():
                raise ValidationError("Data da partida não pode ser no futuro")

            if jogador_brancas_id:
                jogador_brancas = get_jogador(jogador_brancas_id)
                if jogador_brancas and jogador_brancas.data_nascimento:
                    if data_obj < jogador_brancas.data_nascimento:
                        raise ValidationError(
                            f"Data da partida não pode ser anterior à data de nascimento do jogador das brancas"
                        )
            
            if jogador_pretas_id:
                jogador_pretas = get_jogador(jogador_pretas_id)
                if jogador_pretas and jogador_pretas.data_nascimento:
                    if data_obj < jogador_pretas.data_nascimento:
                        raise ValidationError(
                            f"Data da partida não pode ser anterior à data de nascimento do jogador das pretas"
                        )
                        
        except ValueError:
            raise ValidationError("Formato de data inválido. Use YYYY-MM-DD")
    
    if resultado and not validar_resultado(resultado):
        raise ValidationError(f"Resultado inválido. Resultados válidos: {', '.join(RESULTADOS_VALIDOS)}")
    
    if terminacao and not validar_terminacao(terminacao):
        raise ValidationError(f"Terminação inválida. Terminações válidas: {', '.join(TERMINACOES_VALIDAS)}")
    
    if jogador_brancas_id:
        jogador_brancas = get_jogador(jogador_brancas_id)
        if not jogador_brancas:
            raise ValidationError(f"Jogador das brancas não encontrado")
    
    if jogador_pretas_id:
        jogador_pretas = get_jogador(jogador_pretas_id)
        if not jogador_pretas:
            raise ValidationError(f"Jogador das pretas não encontrado")
    
    if jogador_brancas_id and jogador_pretas_id and jogador_brancas_id == jogador_pretas_id:
        raise ValidationError("Os jogadores não podem ser os mesmos")
    
    partida = add_partida(
        evento=evento,
        local_evento=local_evento,
        data_partida=data_partida,
        resultado=resultado,
        terminacao=terminacao,
        controle_tempo=controle_tempo,
        rodada=rodada,
        lances=lances
    )
    
    if jogador_brancas_id:
        adicionar_jogador_partida(partida.id, jogador_brancas_id, "brancas")
    
    if jogador_pretas_id:
        adicionar_jogador_partida(partida.id, jogador_pretas_id, "pretas")

    if resultado and resultado in ['1-0', '0-1', '1/2-1/2']:
        if jogador_brancas_id and jogador_pretas_id:
            atualizar_ratings_jogadores(jogador_brancas_id, jogador_pretas_id, resultado)
    
    return get_partida_com_jogadores(partida.id)

def updatePartida(partida_id: int, **kwargs):
    from src.repositories.PartidaRepository import update_partida, get_partida
    
    partida_existente = get_partida(partida_id)
    if not partida_existente:
        raise ValidationError("Partida não encontrada")
    
    if 'resultado' in kwargs and kwargs['resultado']:
        if not validar_resultado(kwargs['resultado']):
            raise ValidationError(f"Resultado inválido. Resultados válidos: {', '.join(RESULTADOS_VALIDOS)}")
    
    if 'terminacao' in kwargs and kwargs['terminacao']:
        if not validar_terminacao(kwargs['terminacao']):
            raise ValidationError(f"Terminação inválida. Terminações válidas: {', '.join(TERMINACOES_VALIDAS)}")
    
    if 'data_partida' in kwargs and kwargs['data_partida']:
        try:
            if isinstance(kwargs['data_partida'], str):
                data_obj = datetime.strptime(kwargs['data_partida'], "%Y-%m-%d").date()
            else:
                data_obj = kwargs['data_partida']
                
            if data_obj > datetime.now().date():
                raise ValidationError("Data da partida não pode ser no futuro")
        except ValueError:
            raise ValidationError("Formato de data inválido. Use YYYY-MM-DD")
    
    return update_partida(partida_id, **kwargs)

def deletePartida(partida_id):
    partida = get_partida(partida_id)
    if not partida:
        raise ValidationError("Partida não encontrada")
    
    return delete_partida(partida_id)

def adicionarJogadorPartida(partida_id: int, jogador_id: int, cor: str):
    from src.utils.Uteis import validar_cor
    
    if not validar_cor(cor):
        raise ValidationError("Cor deve ser 'brancas' ou 'pretas'")
    
    partida = get_partida(partida_id)
    if not partida:
        raise ValidationError("Partida não encontrada")
    
    jogador = get_jogador(jogador_id)
    if not jogador:
        raise ValidationError("Jogador não encontrado")
    
    return adicionar_jogador_partida(partida_id, jogador_id, cor)

def addPartidaComNomes(
    evento: str = None, 
    local_evento: str = None, 
    data_partida = None, 
    resultado: str = None, 
    terminacao: str = None, 
    controle_tempo: str = None,
    rodada: str = None, 
    lances: str = None,
    jogador_brancas: str = None,
    jogador_pretas: str = None
):
    from src.repositories.JogadorRepository import buscar_jogadores_por_nome
    
    if (not jogador_brancas or jogador_brancas == "Anônimo") and (not jogador_pretas or jogador_pretas == "Anônimo"):
        raise ValidationError("Pelo menos um jogador deve ser identificado")
    
    jogador_brancas_id = None
    jogador_pretas_id = None

    if jogador_brancas and jogador_brancas != "Anônimo":
        jogadores = buscar_jogadores_por_nome(jogador_brancas)
        if jogadores:
            jogador_brancas_id = jogadores[0].id
        else:
            raise ValidationError(f"Jogador das brancas '{jogador_brancas}' não encontrado")
    
    if jogador_pretas and jogador_pretas != "Anônimo":
        jogadores = buscar_jogadores_por_nome(jogador_pretas)
        if jogadores:
            jogador_pretas_id = jogadores[0].id
        else:
            raise ValidationError(f"Jogador das pretas '{jogador_pretas}' não encontrado")

    if (jogador_brancas_id and jogador_pretas_id and 
        jogador_brancas_id == jogador_pretas_id):
        raise ValidationError("Os jogadores não podem ser os mesmos")

    return addPartida(
        evento=evento,
        local_evento=local_evento,
        data_partida=data_partida,
        resultado=resultado,
        terminacao=terminacao,
        controle_tempo=controle_tempo,
        rodada=rodada,
        lances=lances,
        jogador_brancas_id=jogador_brancas_id,
        jogador_pretas_id=jogador_pretas_id
    )

def calcular_variacao_rating(rating_jogador, rating_oponente, resultado, k=32):
   
    esperado = 1 / (1 + 10 ** ((rating_oponente - rating_jogador) / 400))
    
    if resultado == 1:
        pontuacao = 1
    elif resultado == 0.5:
        pontuacao = 0.5
    else:
        pontuacao = 0
    
    variacao = k * (pontuacao - esperado)
    return round(variacao)

def atualizar_ratings_jogadores(jogador_brancas_id, jogador_pretas_id, resultado):
    from src.repositories.JogadorRepository import get_jogador
    from src.services.JogadorService import atualizar_rating_jogador
    
    if not jogador_brancas_id or not jogador_pretas_id:
        return
    
    jogador_brancas = get_jogador(jogador_brancas_id)
    jogador_pretas = get_jogador(jogador_pretas_id)
    
    if not jogador_brancas or not jogador_pretas:
        return
    
    rating_brancas = jogador_brancas.rating or 1200
    rating_pretas = jogador_pretas.rating or 1200
    
    if resultado == '1-0':
        resultado_brancas = 1
        resultado_pretas = 0
    elif resultado == '0-1':
        resultado_brancas = 0
        resultado_pretas = 1
    elif resultado == '1/2-1/2':
        resultado_brancas = 0.5
        resultado_pretas = 0.5
    else:
        return
    
    variacao_brancas = calcular_variacao_rating(rating_brancas, rating_pretas, resultado_brancas)
    variacao_pretas = calcular_variacao_rating(rating_pretas, rating_brancas, resultado_pretas)
    
    atualizar_rating_jogador(jogador_brancas_id, variacao_brancas)
    atualizar_rating_jogador(jogador_pretas_id, variacao_pretas)