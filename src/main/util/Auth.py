from flask_httpauth import HTTPBasicAuth
from models.Usuario import Usuario

auth = HTTPBasicAuth()

@auth.verify_password
def verificacao(login, senha):
    if not (login, senha):
        return False
    return Usuario.query.filter_by(login=login, senha=senha).first()
