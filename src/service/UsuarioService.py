import json
from typing import Tuple
from flask import jsonify, Response
from src.models.Usuario import Usuario


class UsuarioService:
    def listar_usuario(self) -> Tuple[Response, int]:
        return jsonify(Usuario.query.all()), 200


    def salvar_usuario(self, dados) -> Tuple[Response, int]:
        dados = json.loads(dados)
        if 'login' in dados and 'senha' in dados:
            if not Usuario.query.filter_by(login=dados['login']).first():
                usuario = Usuario(login=dados['login'], senha=dados['senha'])
                usuario.salvar()
                return jsonify({'success': 'Inserido com sucesso', 'objeto': usuario}), 201
            else:
                return {'error': 'Usuário já consta na base de dados'}, 409
        return {'error': 'Login ou senha não informados'}, 400


    def modificar_usuario(self, dados) -> Tuple[Response, int]:
        dados = json.loads(dados)
        try:
            usuario = Usuario.query.filter_by(login=dados['login']).first()
        except:
            return {'error': 'Usuário não encontrado'}, 404

        usuario.senha = dados['senha']
        usuario.salvar()
        return jsonify({'success': 'Senha alterada com sucesso!', 'objeto': usuario}), 200


    def apagar_usuario(self, dados) -> Tuple[Response, int]:
        dados = json.loads(dados)
        try:
            usuario = Usuario.query.filter_by(login=dados['login']).first()
        except:
            return {'error': 'Usuário não encontrado'}, 404

        usuario.apagar()
        return {'success': 'Usuário removido do sistema'}, 204
