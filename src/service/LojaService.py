from json import loads
from typing import Tuple
from flask import Response, jsonify
from src.models.Loja import Loja


class LojaService:
    def listar_lojas(self) -> Tuple[Response, int]:
        lojas = Loja.query.all()
        return jsonify(lojas), 200


    def adicionar_loja(self, dados) -> Tuple[Response, int]:
        dados = loads(dados)
        if 'nome' in dados and 'endereco' in dados and 'capacidadeVeiculos' in dados:
            try:
                loja = Loja(
                    nome=dados['nome'],
                    endereco=dados['endereco'],
                    capacidadeVeiculos=dados['capacidadeVeiculos']
                )
                loja.salvar()
                return jsonify({'success': 'Loja criada com sucesso!', 'objeto': loja}), 201
            except:
                return jsonify({'error': 'Aconteceu um erro ao salvar o registro'}), 500
        return jsonify({'error': 'Estão faltando campos no JSON'}), 400


    def modificar_loja(self, dados) -> Tuple[Response, int]:
        dados = loads(dados)
        try:
            loja = Loja.query.filter_by(id=dados['id']).first()
        except:
            return jsonify({'error': 'loja não encontrada'}), 404

        if 'nome' in dados:
            loja.nome = dados['nome']
        if 'endereco' in dados:
            loja.endereco = dados['endereco']
        if 'capacidadeVeiculos' in dados:
            loja.capacidadeVeiculos = dados['capacidadeVeiculos']
        loja.salvar()
        return jsonify({'success': 'Registro alterado com sucesso', 'objeto': loja}), 200


    def remover_loja(self, dados) -> Tuple[Response, int]:
        dados = loads(dados)
        try:
            loja = Loja.query.filter_by(id=dados['id']).first()
        except:
            return jsonify({'error': 'Registro não encontrado'}), 404

        loja.apagar()
        return jsonify({'success': 'Registro apagado'}), 200
