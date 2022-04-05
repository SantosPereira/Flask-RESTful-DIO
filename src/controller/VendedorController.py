import json
from flask import request
from flask_restful import Resource
from src.models.Vendedor import Vendedor
from src.util.Auth import auth

class VendedorController(Resource):
    def __init__(self) -> None:
        super().__init__()

    @auth.login_required
    def get(self):
        vendedores = []
        for vendedor in Vendedor.query.all():
            vendedores.append({
                'id': vendedor.id,
                'nome': vendedor.nome,
                'cpf': vendedor.cpf,
                'endereco': vendedor.endereco,
                'loja_id': vendedor.loja_id,
                'usuario_id': vendedor.usuario.id
            })
        return vendedores

    @auth.login_required
    def post(self):
        dados = json.loads(request.data)
        if 'nome' in dados or 'cpf' in dados or 'endereco' in dados or 'loja_id' in dados or 'usuario_id' in dados:
            Vendedor(
                nome=dados['nome'],
                cpf=dados['cpf'],
                endereco=dados['endereco'],
                loja_id=dados['loja_id'],
                usuario_id=dados['usuario_id']
            )
        return {'success':'Vendedor registrado com sucesso!'}

    @auth.login_required
    def put(self):
        dados = json.loads(request.data)
        try:
            vendedor = Vendedor.query.filter_by(cpf=dados['cpf']).first()
        except:
            return {'error': 'CPF não informado'}
        if 'nome' in dados or 'cpf' in dados or 'endereco' in dados or 'loja_id' in dados or 'usuario_id' in dados:
            vendedor.save(
                nome=dados['nome'],
                cpf=dados['cpf'],
                endereco=dados['endereco'],
                loja_id=dados['loja_id'],
                usuario_id=dados['usuario_id']
            )
        return {'success': 'Modificação realizada'}

    @auth.login_required
    def delete(self):
        dados = json.loads(request.data)
        vendedor = Vendedor.query.filter_by(cpf=dados['cpf']).first()
        vendedor.apagar()
        return {'success':'Registro apagado'}
