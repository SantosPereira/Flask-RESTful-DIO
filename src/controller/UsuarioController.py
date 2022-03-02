import json
from flask import request
from flask_restful import Resource
from util.Auth import auth
from models.Usuario import Usuario

class UsuarioController(Resource):
    def __init__(self) -> None:
        super().__init__()

    @auth.login_required
    def get(self):
        usuarios = Usuario.query.all()
        return usuarios

    def post(self):
        dados = json.loads(request.data)
        if 'login' and 'senha' in dados:
            if not Usuario.query.filter_by(login=dados['login']).first():
                usuario = Usuario(login=dados['login'], senha=dados['senha'])
                usuario.salvar()
                return {'success':'Inserido com sucesso'}
            else:
                return {'error':'Usuário já consta na base de dados'}
        return {'error':'Login ou senha não informados'}

    def put(self):
        return ''

    def delete(self):
        return ''
