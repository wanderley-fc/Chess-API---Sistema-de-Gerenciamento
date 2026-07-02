import re
from datetime import date

FEDERACOES_FIDE = [
    'AFG', 'ALB', 'ALG', 'AND', 'ANG', 'ANT', 'ARG', 'ARM', 'ARU', 'ASA', 'AUS', 
    'AUT', 'AZE', 'BAH', 'BAN', 'BAR', 'BDI', 'BEL', 'BEN', 'BER', 'BHU', 'BIH', 
    'BIZ', 'BLR', 'BOL', 'BOT', 'BRA', 'BRN', 'BRU', 'BUL', 'BUR', 'CAF', 'CAM', 
    'CAN', 'CEY', 'CHA', 'CHI', 'CGO', 'CHN', 'CIV', 'CMR', 'COD', 'COK', 'COL', 
    'COM', 'CPV', 'CRC', 'CRO', 'CUB', 'CYP', 'CZE', 'DEN', 'DJI', 'DMA', 'DOM', 
    'ECU', 'EGY', 'ERI', 'ESA', 'ESP', 'EST', 'ETH', 'FAI', 'FIJ', 'FIN', 'FRA', 
    'FSM', 'GAB', 'GAM', 'GBR', 'GBS', 'GEO', 'GEQ', 'GER', 'GHA', 'GRE', 'GRN', 
    'GUA', 'GUI', 'GUM', 'GUY', 'HAI', 'HKG', 'HON', 'HUN', 'INA', 'IND', 'IRI', 
    'IRL', 'IRQ', 'ISL', 'ISR', 'ISV', 'ITA', 'JAM', 'JOR', 'JPN', 'KAZ', 'KEN', 
    'KGZ', 'KIR', 'KOR', 'KOS', 'KSA', 'KUW', 'LAO', 'LAT', 'LBA', 'LBR', 'LCA', 
    'LES', 'LIB', 'LIE', 'LTU', 'LUX', 'MAC', 'MAD', 'MAR', 'MAS', 'MAW', 'MDA', 
    'MDV', 'MEX', 'MGL', 'MKD', 'MLI', 'MLT', 'MNE', 'MON', 'MOZ', 'MRI', 'MTN', 
    'MYA', 'NAM', 'NCA', 'NED', 'NEP', 'NGR', 'NIG', 'NOR', 'NZL', 'OMA', 'PAK', 
    'PAN', 'PAR', 'PER', 'PHI', 'PLE', 'PLW', 'PNG', 'POL', 'POR', 'PRK', 'PUR', 
    'QAT', 'ROU', 'RSA', 'RUS', 'RWA', 'SAM', 'SEN', 'SEY', 'SIN', 'SKN', 'SLE', 
    'SLO', 'SMR', 'SOL', 'SOM', 'SRB', 'SRI', 'SSD', 'STP', 'SUD', 'SUI', 'SUR', 
    'SVK', 'SWE', 'SWZ', 'SYR', 'TAN', 'TCA', 'TGA', 'THA', 'TJK', 'TKM', 'TLS', 
    'TOG', 'TPE', 'TRI', 'TUN', 'TUR', 'TUV', 'UAE', 'UGA', 'UKR', 'URU', 'USA', 
    'UZB', 'VAN', 'VEN', 'VIE', 'VIN', 'WLS', 'YEM', 'ZAM', 'ZIM'
]

RATING_MINIMO = 0
RATING_MAXIMO = 3000
RATING_PADRAO = 1500

TITULOS_FIDE = ['GM', 'IM', 'FM', 'CM', 'NM', 'WGM', 'WIM', 'WFM', 'WCM']

def validar_federacao(federacao: str) -> bool:

    return federacao.upper() in FEDERACOES_FIDE if federacao else False

def validar_titulo_fide(titulo: str) -> bool:

    return titulo in TITULOS_FIDE if titulo else True  

def validar_nome(nome: str) -> bool:

    if not nome or nome.strip() == '':
        return False
    return bool(re.match(pattern=r"^[a-zA-ZÀ-ÿ\s]+$", string=nome))

def validar_email(email: str) -> bool:

    if not email or email.strip() == '':
        return False
    return bool(re.match(pattern=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", string=email))

def calcular_idade(data_nascimento: date) -> int:

    hoje = date.today()
    idade = hoje.year - data_nascimento.year
    
    if (hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day):
        idade -= 1
    
    return idade

def data_minima_por_idade(idade: int) -> date:
 
    hoje = date.today()
    ano_nascimento = hoje.year - idade
    ano_minimo = 1 
    
    if ano_nascimento < ano_minimo:
        ano_nascimento = ano_minimo
    
    try:
        return date(ano_nascimento, hoje.month, hoje.day)
    except ValueError:
        
        from calendar import monthrange
        try:
            ultimo_dia = monthrange(ano_nascimento, hoje.month)[1]
            return date(ano_nascimento, hoje.month, min(hoje.day, ultimo_dia))
        except:
            
            return date(ano_nascimento, 1, 1)

def data_maxima_por_idade(idade: int) -> date:

    hoje = date.today()
    ano_nascimento = hoje.year - idade - 1
    
    ano_minimo = 1 
    if ano_nascimento < ano_minimo:
        ano_nascimento = ano_minimo
    
    try:
        return date(ano_nascimento, hoje.month, hoje.day)
    except ValueError:
     
        from calendar import monthrange
        try:
            ultimo_dia = monthrange(ano_nascimento, hoje.month)[1]
            return date(ano_nascimento, hoje.month, min(hoje.day, ultimo_dia))
        except:
            
            return date(ano_nascimento, 1, 1)

def validar_rating(rating) -> bool:
   
    if rating is None:
        return True
    
    if not isinstance(rating, (int, float)):
        return False
    
    return RATING_MINIMO <= rating <= RATING_MAXIMO

def validar_numero_positivo(valor: str) -> bool:
   
    if not valor or valor.strip() == '':
        return False
    try:
        numero = int(valor)
        return numero >= 0
    except ValueError:
        return False
    
def filtrar_nome(texto: str) -> str:
    
    if not texto:
        return ""
    
    return re.sub(r'[^a-zA-ZÀ-ÿ\s]', '', texto)

def filtrar_email(texto: str) -> str:
    
    if not texto:
        return ""
  
    return re.sub(r'[^a-zA-Z0-9@._-]', '', texto)

def filtrar_numero_positivo(texto: str) -> str:
   
    if not texto:
        return ""
 
    return re.sub(r'[^\d]', '', texto)

RESULTADOS_VALIDOS = ["1-0", "0-1", "1/2-1/2", "*"]
TERMINACOES_VALIDAS = [
    "Abandono", "Afogamento", "Xeque-mate", "Empate por acordo", 
    "Empate por repetição", "Empate por insuficiencia material", 
    "Empate por regra dos 50 lances", "Timeout", "Vitória por tempo"
]
CORES_VALIDAS = ["brancas", "pretas"]

def validar_resultado(resultado: str) -> bool:
  
    return resultado in RESULTADOS_VALIDOS if resultado else True

def validar_terminacao(terminacao: str) -> bool:
    
    return terminacao in TERMINACOES_VALIDAS if terminacao else True

def validar_cor(cor: str) -> bool:
    
    return cor in CORES_VALIDAS


