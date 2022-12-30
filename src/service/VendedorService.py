from json import loads
from typing import Tuple
from flask import jsonify, Response
from src.models.Vendedor import Vendedor

class VendedorService:
    def listar_vendedores(self) -> Tuple[Response, int]:
        vendedores = Vendedor.query.all()
        return jsonify(vendedores), 200

    def salvar_vendedor(self, dados) -> Tuple[Response, int]:
        dados = loads(dados)
        if 'nome' in dados or 'cpf' in dados or 'endereco' in dados or 'loja_id' in dados or 'usuario_id' in dados:
            vendedor = Vendedor(
                nome=dados['nome'],
                cpf=dados['cpf'],
                endereco=dados['endereco'],
                loja_id=dados['loja_id'],
                usuario_id=dados['usuario_id']
            )
            vendedor.salvar()
        return jsonify({'success':'Vendedor registrado com sucesso!', 'objeto': vendedor}), 200


    def modificar_vendedor(self, dados) -> Tuple[Response, int]:
        dados = loads(dados)
        try:
            vendedor = Vendedor.query.filter_by(id=dados['id']).first()
        except:
            return {'error': 'CPF não informado'}
        if 'nome' in dados and 'cpf' in dados and 'endereco' in dados and 'loja_id' in dados and 'usuario_id' in dados:
            vendedor.nome=dados['nome']
            vendedor.cpf=dados['cpf']
            vendedor.endereco=dados['endereco']
            vendedor.loja_id=dados['loja_id']
            vendedor.usuario_id=dados['usuario_id']
            vendedor.salvar()
        return jsonify({'success': 'Modificação realizada', 'objeto': vendedor}), 200


    def apagar_vendedor(self, dados) -> Tuple[Response, int]:
        dados = loads(dados)
        vendedor = Vendedor.query.filter_by(cpf=dados['cpf']).first()
        vendedor.apagar()
        return {'success':'Registro apagado'}
