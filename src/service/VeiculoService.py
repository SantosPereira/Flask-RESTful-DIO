import json
from typing import Tuple
from flask import jsonify, Response
from src.models.Veiculo import Veiculo

class VeiculoService:
    def listar_veiculos(self) -> Tuple[Response, int]:
        veiculos = Veiculo.query.all()
        return jsonify(veiculos), 200

    
    def adcionar_veiculo(self, dados) -> Tuple[Response, int]:
        dados = json.loads(dados)
        veiculo = Veiculo(    
            id=dados['id'],
            modelo=dados['modelo'],
            versao=dados['versao'],
            marca=dados['marca'],
            combustivel=dados['combustivel'],
            potencia=dados['potencia'],
            peso=dados['peso'],
            computadorBordo=dados[' computadorBordo'],
            arCondicionado=dados['arCondicionado'],
            preco=dados['preco'],
        )
        veiculo.salvar()
        return jsonify(veiculo), 201


    def modificar_veiculo(self, dados) -> Tuple[Response, int]:
        dados = json.loads(dados)
        try:
            veiculo = Veiculo.query.filter_by(id=dados['id']).first()
        except:
            return jsonify('Não encontrado'), 404

        veiculo.id=dados['id']
        veiculo.modelo=dados['modelo']
        veiculo.versao=dados['versao']
        veiculo.marca=dados['marca']
        veiculo.combustivel=dados['combustivel']
        veiculo.potencia=dados['potencia']
        veiculo.peso=dados['peso']
        veiculo.computadorBordo=dados[' computadorBordo']
        veiculo.arCondicionado=dados['arCondicionado']
        veiculo.preco=dados['preco']
        
        veiculo.salvar()
        return jsonify(veiculo), 200

    def apagar_veiculo(self, dados) -> Tuple[Response, int]:
        dados = json.loads(dados)
        try:
            veiculo = Veiculo.query.filter_by(id=dados['id']).first()
        except:
            return jsonify("erro"), 500
        veiculo.apagar()
        return jsonify('Apagado'), 200
