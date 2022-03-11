from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from util.Cursor import Base, db_session
from Cliente import Cliente
from Veiculo import Veiculo
from Vendedor import Vendedor

class Venda(Base):
    __tablename__ = 'venda'
    id = Column(Integer, primary_key=True)
    valor = Column(Integer)
    metodoPagamento = Column(String(20))
    desconto = Column(Integer)
    cliente_id = Column(Integer, ForeignKey('cliente.id'))
    cliente = relationship('Cliente')
    veiculo_id = Column(Integer, ForeignKey('veiculo.id'))
    veiculo = relationship('Veiculo')
    vendedor_id = Column(Integer, ForeignKey('vendedor.id'))
    vendedor = relationship('Vendedor')

    def salvar(self) -> None:
        db_session.add(self)
        db_session.commit()


    def apagar(self) -> None:
        db_session.delete(self)
        db_session.commit()


    def __repr__(self) -> str:
        return f'<Venda {self.id}>'