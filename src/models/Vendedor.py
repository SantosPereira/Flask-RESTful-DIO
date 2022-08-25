from dataclasses import dataclass
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from src.util.Cursor import Base, db_session
from src.models.Loja import Loja
from src.models.Usuario import Usuario

@dataclass
class Vendedor(Base):
    __tablename__ = 'vendedor'
    id: int = Column(Integer, primary_key=True)
    nome: str = Column(String(100), nullable=False)
    cpf: int = Column(Integer, unique=True, nullable=False)
    endereco: str = Column(String(80))
    loja_id: int = Column(Integer, ForeignKey('loja.id'))
    loja = relationship('Loja')
    usuario_id: int = Column(Integer, ForeignKey('usuario.id'))
    usuario = relationship('Usuario')

    def salvar(self) -> None:
        db_session.add(self)
        db_session.commit()


    def apagar(self) -> None:
        db_session.delete(self)
        db_session.commit()


    def __repr__(self) -> str:
        return f'<Vendedor {self.id}:{self.nome}:{self.cpf}>'