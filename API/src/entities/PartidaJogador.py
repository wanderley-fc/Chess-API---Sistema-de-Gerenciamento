from sqlalchemy import Column, Integer, String, ForeignKey
from src.entities.database import Base

class PartidaJogador(Base):
    __tablename__ = "partida_jogador"

    id = Column(
        "id",
        Integer,
        primary_key=True,
        autoincrement=True
    )
    partida_id = Column(
        "partida_id", 
        Integer, 
        ForeignKey("partida.id"),
        nullable=False
    )
    jogador_id = Column(
        "jogador_id",
        Integer,
        ForeignKey("jogador.id"), 
        nullable=False
    )
    cor = Column("cor", String(6), nullable=False)

    def __repr__(self):
        return f"<PartidaJogador(partida_id={self.partida_id}, jogador_id={self.jogador_id}, cor='{self.cor}')>"