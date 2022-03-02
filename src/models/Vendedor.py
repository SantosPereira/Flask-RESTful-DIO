from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from util.Cursor import Base, db_session
from Loja import Loja
from Usuario import Usuario

class Vendedor(Base):
    __tablename__ = 'vendedor'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    cpf = Column(Integer, unique=True, nullable=False)
    endereco = Column(String(80))
    loja_id = Column(Integer, ForeignKey('loja.id'))
    loja = relationship('Loja')
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    usuario = relationship('Usuario')

    def salvar(self) -> None:
        db_session.add(self)
        db_session.commit()


    def apagar(self) -> None:
        db_session.delete(self)
        db_session.commit()


    def __repr__(self) -> str:
        return f'<Vendedor {self.id}:{self.nome}:{self.cpf}>'