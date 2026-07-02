from sqlalchemy import Column, Integer, String, Date
from src.entities.database import Base
from datetime import date

class Jogador(Base):
    __tablename__ = "jogador"
    
    id = Column(
        "id",
        Integer,
        primary_key=True,
        autoincrement=True
    )
    nome = Column("nome", String(100), nullable=False)
    federacao = Column("federacao", String(3), nullable=True)
    rating = Column("rating", Integer, default=1500, nullable=False) 
    data_nascimento = Column("data_nascimento", Date, nullable=False)
    titulo_fide = Column("titulo_fide", String(3), nullable=True)
    email = Column("email", String(100), nullable=False, unique=True)
    data_cadastro = Column("data_cadastro", Date, default=date.today)

    def __repr__(self):
        return f"<Jogador(id={self.id}, nome='{self.nome}', rating={self.rating})>"