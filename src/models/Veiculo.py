from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from util.Cursor import Base, db_session

class Veiculo(Base):
    __tablename__ = 'veiculo'
    id = Column(Integer, primary_key=True)
    modelo = Column(String(20), nullable=False)
    versao = Column(String(10))
    marca = Column(String(25))
    combustivel = Column(String(25))
    potencia = Column(String(10))
    peso = Column(Integer)
    computadorBordo = Column(Boolean)
    arCondicionado = Column(Boolean)
    preco = Column(Integer, nullable=False)


    def salvar(self) -> None:
        db_session.add(self)
        db_session.commit()


    def apagar(self) -> None:
        db_session.delete(self)
        db_session.commit()


    def __repr__(self) -> str:
        return f'<Veículo {self.modelo}:{self.id}>'
