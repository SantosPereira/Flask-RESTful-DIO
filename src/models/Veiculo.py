from dataclasses import dataclass
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from src.util.Cursor import Base, db_session

@dataclass
class Veiculo(Base):
    __tablename__ = 'veiculo'
    id: int = Column(Integer, primary_key=True)
    modelo: str = Column(String(20), nullable=False)
    versao: str = Column(String(10))
    marca: str = Column(String(25))
    combustivel: str = Column(String(25))
    potencia: str = Column(String(10))
    peso: int = Column(Integer)
    computadorBordo: bool = Column(Boolean)
    arCondicionado: bool = Column(Boolean)
    preco: int = Column(Integer, nullable=False)


    def salvar(self) -> None:
        db_session.add(self)
        db_session.commit()


    def apagar(self) -> None:
        db_session.delete(self)
        db_session.commit()


    def __repr__(self) -> str:
        return f'<Veículo {self.modelo}:{self.id}>'
