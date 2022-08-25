from dataclasses import dataclass
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from src.util.Cursor import Base, db_session

@dataclass
class Loja(Base):
    __tablename__ = 'loja'
    id: int = Column(Integer, primary_key=True)
    nome: str = Column(String(30), unique=True)
    endereco: str = Column(String(120))
    capacidadeVeiculos: int = Column(Integer)

    def salvar(self) -> None:
        db_session.add(self)
        db_session.commit()


    def apagar(self) -> None:
        db_session.delete(self)
        db_session.commit()


    def __repr__(self) -> str:
        return f'<Loja {self.id}:{self.endereco}>'