import json
from flask import jsonify
from src.models.Vendedor import Vendedor

class VendedorService:
    def listar_vendedores(self):
        vendedores = Vendedor.query.all()
        return jsonify(vendedores)

    def salvar_vendedor(self, dados):
        dados = json.loads(dados)
        if 'nome' in dados or 'cpf' in dados or 'endereco' in dados or 'loja_id' in dados or 'usuario_id' in dados:
            vendedor = Vendedor(
                nome=dados['nome'],
                cpf=dados['cpf'],
                endereco=dados['endereco'],
                loja_id=dados['loja_id'],
                usuario_id=dados['usuario_id']
            )
            vendedor.salvar()
        return {'success':'Vendedor registrado com sucesso!', 'objeto': jsonify(vendedor)}


    def modificar_vendedor(self, dados):
        dados = json.loads(dados)
        try:
            vendedor = Vendedor.query.filter_by(cpf=dados['cpf']).first()
        except:
            return {'error': 'CPF não informado'}
        if 'nome' in dados or 'cpf' in dados or 'endereco' in dados or 'loja_id' in dados or 'usuario_id' in dados:
            vendedor.nome=dados['nome'],
            vendedor.cpf=dados['cpf'],
            vendedor. endereco=dados['endereco'],
            vendedor.loja_id=dados['loja_id'],
            vendedor. usuario_id=dados['usuario_id']
            vendedor.salvar()
        return {'success': 'Modificação realizada', 'objeto': jsonify(vendedor)}

    def apagar_vendedor(self, dados):
        dados = json.loads(dados)
        vendedor = Vendedor.query.filter_by(cpf=dados['cpf']).first()
        vendedor.apagar()
        return {'success':'Registro apagado'}
