from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from src.util.Cursor import Base, db_session

class Loja(Base):
    __tablename__ = 'loja'
    id = Column(Integer, primary_key=True)
    nome = Column(String(30), unique=True)
    endereco = Column(String(120))
    capacidadeVeiculos = Column(Integer)

    def salvar(self) -> None:
        db_session.add(self)
        db_session.commit()


    def apagar(self) -> None:
        db_session.delete(self)
        db_session.commit()


    def __repr__(self) -> str:
        return f'<Loja {self.id}:{self.endereco}>'