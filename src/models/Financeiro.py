from dataclasses import dataclass
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from src.util.Cursor import Base, db_session
from src.models.Loja import Loja

@dataclass
class Financeiro(Base):
    __tablename__ = 'financeiro'
    id: int = Column(Integer, primary_key=True)
    loja_id: int = Column(Integer, ForeignKey('loja.id')    )
    loja = relationship('Loja')
    

    def salvar(self) -> None:
        db_session.add(self)
        db_session.commit()


    def apagar(self) -> None:
        db_session.delete(self)
        db_session.commit()


    def __repr__(self) -> str:
        return f'<Financeiro {self.id}>'