from sqlalchemy import Column, Integer, String, Date, Text
from src.entities.database import Base

class Partida(Base):
    __tablename__ = "partida"
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    evento = Column("evento", String(100), nullable=True)
    local_evento = Column("local_evento", String(100), nullable=True)
    data_partida = Column("data_partida", Date, nullable=True)
    resultado = Column("resultado", String(7), nullable=True)
    terminacao = Column("terminacao", String(30), nullable=True)
    controle_tempo = Column("controle_tempo", String(20), nullable=True)
    rodada = Column("rodada", String(20), nullable=True)
    lances = Column("lances", Text, nullable=True)
    
    def __repr__(self):
        return f"<Partida(id={self.id}, evento='{self.evento}', resultado='{self.resultado}')>"