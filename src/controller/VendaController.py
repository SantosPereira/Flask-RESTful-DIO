import json
from flask import request, jsonify
from flask_restful import Resource
from src.models.Cliente import Cliente
from src.models.Venda import Venda
from src.util.Auth import auth

class VendaController(Resource):
    def __init__(self) -> None:
        super().__init__()

    def get(self):
        return jsonify(Venda.query.all())

    @auth.login_required
    def post(self):
        dados = json.loads(request.data)
        venda = Venda(
            valor=dados['valor'],
            metodoPagamento=dados['metodoPagamento'],
            desconto=dados['desconto'],
            cliente_id=dados['cliente_id'],
            veiculo_id=dados['veiculo_id'],
            vendedor_id=dados['vendedor_id']
        )
        venda.salvar()
        return jsonify(venda)

    @auth.login_required
    def put(self):
        dados = json.loads(request.data)
        venda = Venda.query.filter_by(id=dados['id']).first()
        venda.valor=dados['valor'],
        venda.metodoPagamento=dados['metodoPagamento'],
        venda.desconto=dados['desconto'],
        venda.cliente_id=dados['cliente_id'],
        venda.veiculo_id=dados['veiculo_id'],
        venda.vendedor_id=dados['vendedor_id']
        venda.salvar()
        return jsonify(venda)

    @auth.login_required
    def delete(self):
        dados = json.loads(request.data)
        venda = Venda.query.filter_by(id=dados['id']).first()
        venda.apagar()
        return {'success':'Registro apagado'}
