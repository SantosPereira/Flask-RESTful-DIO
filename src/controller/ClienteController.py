import json
from flask import request, jsonify
from flask_restful import Resource
from src.util.Auth import auth
from src.models.Cliente import Cliente


class ClienteController(Resource):
    def __init__(self) -> None:
        super().__init__()

    @auth.login_required
    def get(self):
        clientes = Cliente.query.all()
        return jsonify(clientes)

    @auth.login_required
    def post(self):
        dados = json.loads(request.data)
        # TODO ~~> validar cpf
        if 'nome' in dados and 'cpf' in dados and 'endereco' in dados and 'clubeBeneficios' in dados:
            try:
                cliente = Cliente(
                    nome=dados['nome'],
                    cpf=dados['cpf'],
                    endereco=dados['endereco'],
                    clubeBeneficios=dados['clubeBeneficios']
                )
                cliente.salvar()
                return jsonify({'success': 'Cliente criado com sucesso!', 'objeto': cliente})
            except:
                return {'error': 'Aconteceu um erro ao salvar o registro'}
        return {'error': 'Estão faltando campos no JSON'}

    @auth.login_required
    def put(self):
        dados = json.loads(request.data)
        try:
            cliente = Cliente.query.filter_by(cpf=dados['cpf']).first()
        except:
            return {'error': 'CPF não informado'}

        if 'nome' in dados:
            cliente.nome = dados['nome']
        if 'endereco' in dados:
            cliente.endereco = dados['endereco']
        if 'clubeBeneficios' in dados:
            cliente.clubeBeneficios = dados['clubeBeneficios']
        cliente.salvar()
        return jsonify({'success': 'Registro alterado com sucesso', 'objeto': cliente})

    @auth.login_required
    def delete(self):
        dados = json.loads(request.data)
        try:
            cliente = Cliente.query.filter_by(cpf=dados['cpf']).first()
        except:
            return {'error': 'Registro não encontrado'}

        cliente.apagar()
        return {'success': 'Registro apagado'}
