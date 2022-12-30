from json import loads
from typing import Tuple
from flask import Response, jsonify
from src.models.Financeiro import Financeiro


class FinanceiroService:
    def listar_financeiros(self) -> Tuple[Response, int]:
        financeiros = Financeiro.query.all()
        return jsonify(financeiros), 200


    def adicionar_financeiro(self, dados) -> Tuple[Response, int]:
        dados = loads(dados)
        try:
            financeiro = Financeiro(
                loja_id=dados['loja_id']
            )
            financeiro.salvar()
            return jsonify({'success': 'Financeiro criado com sucesso!', 'objeto': financeiro}), 201
        except:
            return jsonify({'error': 'Aconteceu um erro ao salvar o registro'}), 500


    def modificar_financeiro(self, dados) -> Tuple[Response, int]:
        dados = loads(dados)
        try:
            financeiro = Financeiro.query.filter_by(id=dados['id']).first()
        except:
            return jsonify({'error': 'Registro não encontrado'}), 404

        if 'loja_id' in dados:
            financeiro.loja_id = dados['loja_id']
        financeiro.salvar()
        return jsonify({'success': 'Registro alterado com sucesso', 'objeto': financeiro}), 200


    def remover_financeiro(self, dados) -> Tuple[Response, int]:
        dados = loads(dados)
        try:
            financeiro = Financeiro.query.filter_by(id=dados['id']).first()
        except:
            return jsonify({'error': 'Registro não encontrado'}), 404

        financeiro.apagar()
        return jsonify({'success': 'Registro apagado'}), 200
