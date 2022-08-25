from dataclasses import dataclass
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from src.util.Cursor import Base, db_session

@dataclass
class Usuario(Base):
    __tablename__ = 'usuario'
    id: int = Column(Integer, primary_key=True)
    login: str = Column(String(20), unique=True)
    senha: str = Column(String(20), nullable=False)

    def salvar(self) -> None:
        db_session.add(self)
        db_session.commit()


    def apagar(self) -> None:
        db_session.delete(self)
        db_session.commit()


    def __repr__(self) -> str:
        return f'<Usuário {self.login}>'