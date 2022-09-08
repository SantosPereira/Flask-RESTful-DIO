import json
from typing import Tuple
from flask import Response, jsonify
from src.models.Venda import Venda


class VendaService:
    def listar_vendas(self) -> Tuple[Response, int]:
        vendas = Venda.query.all()
        return jsonify(vendas), 200


    def adicionar_venda(self, dados) -> Tuple[Response, int]:
        dados = json.loads(dados)
        venda = Venda(
            valor=dados['valor'],
            metodoPagamento=dados['metodoPagamento'],
            desconto=dados['desconto'],
            cliente_id=dados['cliente_id'],
            veiculo_id=dados['veiculo_id'],
            vendedor_id=dados['vendedor_id']
        )
        venda.salvar()
        return jsonify(venda), 200


    def modificar_venda(self, dados) -> Tuple[Response, int]:
        dados = json.loads(dados)
        venda = Venda.query.filter_by(id=dados['id']).first()
        venda.valor=dados['valor'],
        venda.metodoPagamento=dados['metodoPagamento'],
        venda.desconto=dados['desconto'],
        venda.cliente_id=dados['cliente_id'],
        venda.veiculo_id=dados['veiculo_id'],
        venda.vendedor_id=dados['vendedor_id']
        venda.salvar()
        return jsonify(venda), 200


    def remover_venda(self, dados) -> Tuple[Response, int]:
        dados = json.loads(dados)
        venda = Venda.query.filter_by(id=dados['id']).first()
        venda.apagar()
        return jsonify({'success': 'Registro apagado'}), 200
        