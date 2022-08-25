from dataclasses import dataclass
from multiprocessing.connection import Client
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from src.util.Cursor import Base, db_session
from src.models.Cliente import Cliente
from src.models.Veiculo import Veiculo
from src.models.Vendedor import Vendedor

@dataclass
class Venda(Base):
    __tablename__ = 'venda'
    id: int = Column(Integer, primary_key=True)
    valor: int = Column(Integer)
    metodoPagamento: str = Column(String(20))
    desconto: int = Column(Integer)
    cliente_id: int = Column(Integer, ForeignKey('cliente.id'))
    cliente = relationship('Cliente')
    veiculo_id: int = Column(Integer, ForeignKey('veiculo.id'))
    veiculo = relationship('Veiculo')
    vendedor_id: int = Column(Integer, ForeignKey('vendedor.id'))
    vendedor = relationship('Vendedor')

    def salvar(self) -> None:
        db_session.add(self)
        db_session.commit()


    def apagar(self) -> None:
        db_session.delete(self)
        db_session.commit()


    def __repr__(self) -> str:
        return f'<Venda {self.id}>'