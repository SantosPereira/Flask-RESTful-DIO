from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Cria banco de dados, no nosso caso um banco SQLite
engine = create_engine('sqlite:///banco.db')
# Cria uma sessão no banco
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property() 

# Cria a base na primeira execução
def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db()
