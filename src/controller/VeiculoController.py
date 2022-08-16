import json
from flask import request
from flask_restful import Resource
from ..models.Usuario import Usuario
from src.util.Auth import auth
from src.models.Veiculo import Veiculo

class VeiculoController(Resource):
    def __init__(self) -> None:
        super().__init__()

    def get(self):
        veiculos = [
            {
                'id':veiculo.id,
                'modelo':veiculo.modelo,
                'versao':veiculo.versao,
                'marca':veiculo.marca,
                'combustivel':veiculo.combustivel,
                'potencia':veiculo.potencia,
                'peso':veiculo.peso,
                'computadorBordo':veiculo.computadorBordo, 
                'arCondicionado':veiculo.arCondicionado,
                'preco':veiculo.preco
            } for veiculo in Veiculo.query.all()]
        return veiculos

    @auth.login_required
    def post(self):
        dados = json.loads(request.data)
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
        return veiculo

    @auth.login_required
    def put(self):
        dados = json.loads(request.data)
        try:
            veiculo = Veiculo.query.filter_by(id=dados['id']).first()
        except:
            return 'Não encontrado'

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
        return veiculo

    @auth.login_required
    def delete(self):
        dados = json.loads(request.data)
        try:
            veiculo = Veiculo.query.filter_by(id=dados['id']).first()
        except:
            return "erro"
        veiculo.apagar()
        return 'Apagado'
