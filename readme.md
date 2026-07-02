# Chess API - Sistema de Gerenciamento

Sistema completo para gerenciamento de jogadores e partidas de xadrez com interface gráfica e API REST.

## 📋 Requisitos

- **Python 3.12.4**  
  [Download oficial - Python 3.12.4](https://www.python.org/downloads/release/python-3124/) 

## ⚙️ Configuração

### Variáveis de ambiente (Windows)

```cmd
set PYTHON_HOME=<caminho_para_o_python>
set PATH=%PYTHON_HOME%\bin;%PATH%
```

### Variáveis de ambiente (Linux/macOS)

```bash
export PYTHON_HOME=/caminho/para/o/python
export PATH=$PYTHON_HOME/bin:$PATH
```  

### Ambiente virtual venv (Windows)

```cmd
python -m venv venv
venv\Scripts\activate
```

### Ambiente virtual venv (Linux/macOS)

```bash
python -m venv venv
source venv/bin/activate
```  

### Dependências

```bash
(venv) cd API
(venv) pip install -r requirements.txt
```  

### Banco de dados

```
- Crie o banco chess_db (PostgreSQL) conforme o chess_db.txt
- Configure a string de conexão no arquivo ChessAPI/API/src/_init_py

'postgresql://usuario:senha@localhost:5432/chess_db'
```  

## 🚀 Como Executar

### ⚠️ IMPORTANTE: Execute em DOIS terminais separados

### Terminal 1 - Backend (API)
```bash
(venv) cd API
(venv) flask run
```
API rodando em: http://localhost:5000/xadrez

### Terminal 2 - Frontend (Interface Gráfica)
```bash
(venv) cd API/src/views
(venv) python mainframe.py
```

## 🏗️ Estrutura do Projeto

```
ChessAPI/           
├── .venv/           
├── API/             
│   ├── src/
│   │   ├── controllers/
│   │   ├── entities/
│   │   ├── repositories/
│   │   ├── routes/
│   │   ├── services/
│   │   ├── utils/
│   │   ├── views/
│   │   └──__init__.py
│   └─── appy.py
├── readme.md
├── chess_db.txt
└── requirements.txt
```

## 📌 Escopo do Projeto

Funcionalidades disponíveis no sistema:

### ✅ Cadastro de Jogadores

- Inserir, editar e remover
- Dados de registro: `nome`, `email`, `data de nascimento`, `título fide`, `rating`, `data de registro`

### ✅ Cadastro de Partidas

- Inserir e remover
- Dados de registro: `jogador de brancas`, `jogador de pretas`, `data`, `evento`, `local`, `controle de tempo`, `rodada`, `terminação`, `resultado`, `lances`
---

# ♟️ Regras de Negócio - Sistema de Gerenciamento de Xadrez

## 📋 Cadastro de Jogadores

### 1. 👤 Dados Obrigatórios
- **Nome** - Campo obrigatório
- **Email** - Campo obrigatório e único  
- **Data de Nascimento** - Campo obrigatório

### 2. 🎯 Validação de Nome
- ✅ **Aceita**: Letras, acentos, espaços
- ✅ **Aceita**: Atualizações
- ❌ **Não aceita**: Números, caracteres especiais (@, #, $, etc.)
- 🔄 **Único**: Não pode haver dois jogadores com mesmo nome

### 3. 📧 Validação de Email
- ✅ **Formato válido**: deve conter "@" e domínio
- ✅ **Aceita**: Atualizações
- 🔄 **Único**: Não pode haver dois jogadores com mesmo email
- ❌ **Não aceita**: Emails duplicados

### 4. 🎂 Data de nascimento e Validação de Idade
- ✅ **Idade mínima**: 5 anos
- ❌ **Não aceita**: Jogadores com menos de 5 anos
- ❌ **Não aceita**: Datas futuras
- 🔒 **Não editável**: Definida apenas no momento do cadastro
- ⚠️ **Cálculo**: Baseado na data de nascimento vs data atual

### 5. 🌍 Federação (Opcional)
- ✅ **Aceita**: Códigos de 3 letras reconhecidos pela FIDE (BRA, USA, RUS, etc.)
- ✅ **Vazio/NULL**: Jogador pode não ter federação
- ✅ **Aceita**: Atualizações
- ❌ **Não aceita**: Códigos não reconhecidos pela FIDE

### 6. ⭐ Título FIDE (Opcional)
- ✅ **Aceita**: GM, IM, NM, FM, CM, WFM, WIM, WGM 
- ✅ **Vazio/NULL**: Jogador pode não ter título
- ✅ **Aceita**: Atualizações
- ❌ **Não aceita**: Títulos não reconhecidos

### 7. 📊 Rating 
- ✅ **Valor padrão**: 1500 (se não informado)
- ✅ **Range válido**: 0 a 3000
- ❌ **Não aceita**: Valores negativos ou acima de 3000
- 🔒 **Não editável**: O cadastro de novas partidas movimenta o rating

### 8. 📅 Data de Cadastro
- ✅ **Automático**: Definida como data atual do sistema
- 🔒 **Não editável**: Definida apenas no momento do cadastro

---

## 📋 Cadastro de Partidas

### 1. 👤 Jogadores Obrigatórios
- **Jogador das Brancas** - Campo obrigatório
- **Jogador das Pretas** - Campo obrigatório

### 2. 🎯 Validação de Jogadores
- ❌ **Não aceita**: Jogadores não cadastrados 
- 🔄 **Diferentes**: Os dois jogadores não podem ser os mesmos 

### 3. 📅 Validação de Data
- ✅ **Data da Partida** - Campo obrigatório
- ❌ **Não aceita**: Datas futuras
- ⚠️ **Validação**: Data não pode ser anterior à data de nascimento dos jogadores

### 4. 🏆 Resultado (Opcional)
- ✅ **Aceita**: Resultados válidos: "1-0", "0-1", "1/2-1/2"
- ✅ **Vazio/NULL**: Partida pode não ter resultado definido
- ❌ **Não aceita**: Resultados fora do padrão FIDE
- ⚠️ ***IMPORTANTE***: Apenas partidas com resultado registrado movimentam rating

### 5. 🔚 Terminação (Opcional)
- ✅ **Aceita**: Terminações válidas
- ✅ **Vazio/NULL**: Partida pode não ter terminação definida
- ❌ **Não aceita**: Terminações não reconhecidas

### 6. ⏱️ Time Control (Opcional)
- ✅ **Aceita**: Apenas números e sinal de + (ex: "60+30", "10+0", "180")
- ✅ **Formato**: Minutos + segundos de incremento
- ❌ **Não aceita**: Letras ou caracteres especiais (exceto +)

### 7. 🏁 Rodada (Opcional)
- ✅ **Aceita**: Números e texto para identificação da rodada
- ✅ **Vazio/NULL**: Partida pode não ter rodada definida

### 8. 📝 Lances (Opcional)
- ✅ **Aceita**: Notação algébrica de xadrez
- ✅ **Vazio/NULL**: Partida pode não ter lances registrados
- 📏 **Formato**: Sequência de movimentos em notação padrão

### 9. 🎪 Evento e Local (Opcionais)
- ✅ **Evento** - Nome do torneio ou evento
- ✅ **Local do Evento** - Local onde a partida foi disputada
- ✅ **Vazio/NULL**: Campos opcionais

---

## ⚠️ Casos de Erro Comuns - Partidas

| Campo | Mensagem de Erro | Motivo |
|-------|------------------|---------|
| **Jogadores** | "Selecione o jogador das Brancas/Pretas!" | Campo obrigatório vazio |
| **Jogadores** | "Os jogadores não podem ser os mesmos!" | Mesmo jogador para ambos os lados |
| **Jogadores** | "Pelo menos um jogador deve ser identificado!" | Ambos os jogadores como "Anônimo" |
| **Data** | "A data da partida não pode ser no futuro!" | Data futura selecionada |
| **Data** | "Data da partida é anterior à data de nascimento do jogador!" | Inconsistência temporal |

---

### 🏆 Exemplo: Partida de Torneio
```json
{
  "jogador_brancas": "Magnus Carlsen",
  "jogador_pretas": "Hikaru Nakamura",
  "evento": "Campeonato Mundial 2023",
  "local_evento": "Astana, Cazaquistão",
  "data_partida": "2023-04-15",
  "resultado": "1-0",
  "terminacao": "Normal",
  "controle_tempo": "120+30",
  "rodada": "7",
  "lances": "1. e4 e5 2. Nf3 Nc6 3. Bb5 a6"
}
```
---
## 📘 Licença

Este projeto é de uso **livre**, inclusive para fins comerciais ou acadêmicos, **desde que seja feita a devida atribuição aos autores**.

> Autor: **Fernando Wanderley**    
> Referência: Chess API - Sistema de Gerenciamento
