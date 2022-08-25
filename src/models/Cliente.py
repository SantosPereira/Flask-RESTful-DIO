from dataclasses import dataclass
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from src.models.Usuario import Usuario
from src.util.Cursor import Base, db_session

@dataclass
class Cliente(Base):
    __tablename__ = 'cliente'
    id: int = Column(Integer, primary_key=True)
    nome: str = Column(String(100), nullable=False)
    cpf: int = Column(Integer, unique=True, nullable=False)
    endereco: str = Column(String(80))
    clubeBeneficios: bool = Column(Boolean)

    def salvar(self) -> None:
        db_session.add(self)
        db_session.commit()


    def apagar(self) -> None:
        db_session.delete(self)
        db_session.commit()


    def __repr__(self) -> str:
        return f'<Cliente {self.id}:{self.nome}>'