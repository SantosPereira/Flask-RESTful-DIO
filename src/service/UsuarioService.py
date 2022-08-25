import json
from flask import jsonify
from src.models.Usuario import Usuario

class UsuarioService:
    def listar_usuario(self):
        return jsonify(Usuario.query.all())

    def salvar_usuario(self, dados):
        dados = json.loads(dados)
        if 'login' in dados and 'senha' in dados:
            if not Usuario.query.filter_by(login=dados['login']).first():
                usuario = Usuario(login=dados['login'], senha=dados['senha'])
                usuario.salvar()
                return jsonify({'success': 'Inserido com sucesso', 'objeto': usuario})
            else:
                return {'error': 'Usuário já consta na base de dados'}
        return {'error': 'Login ou senha não informados'}

    def modificar_usuario(self, dados):
        dados = json.loads(dados)
        try:
            usuario = Usuario.query.filter_by(login=dados['login']).first()
        except:
            return {'error': 'Usuário não encontrado'}

        usuario.senha = dados['senha']
        usuario.salvar()
        return jsonify({'success': 'Senha alterada com sucesso!', 'objeto': usuario})

    def apagar_usuario(self, dados):
        dados = json.loads(dados)
        try:
            usuario = Usuario.query.filter_by(login=dados['login']).first()
        except:
            return {'error': 'Usuário não encontrado'}

        usuario.apagar()
        return {'success': 'Usuário removido do sistema'}
