import json
from flask import request, jsonify
from flask_restful import Resource
from src.util.Auth import auth
from src.models.Usuario import Usuario


class UsuarioController(Resource):
    def __init__(self) -> None:
        super().__init__()

    @auth.login_required
    def get(self):
        usuarios = Usuario.query.all()
        return jsonify(usuarios)

    def post(self):
        dados = json.loads(request.data)
        if 'login' in dados and 'senha' in dados:
            if not Usuario.query.filter_by(login=dados['login']).first():
                usuario = Usuario(login=dados['login'], senha=dados['senha'])
                usuario.salvar()
                return jsonify({'success': 'Inserido com sucesso', 'objeto': usuario})
            else:
                return {'error': 'Usuário já consta na base de dados'}
        return {'error': 'Login ou senha não informados'}

    @auth.login_required
    def put(self):
        dados = json.loads(request.data)
        try:
            usuario = Usuario.query.filter_by(login=dados['login']).first()
        except:
            return {'error': 'Usuário não encontrado'}

        usuario.senha = dados['senha']
        usuario.salvar()
        return jsonify({'success': 'Senha alterada com sucesso!', 'objeto': usuario})

    @auth.login_required
    def delete(self):
        dados = json.loads(request.data)
        try:
            usuario = Usuario.query.filter_by(login=dados['login']).first()
        except:
            return {'error': 'Usuário não encontrado'}

        usuario.apagar()
        return {'success': 'Usuário removido do sistema'}
