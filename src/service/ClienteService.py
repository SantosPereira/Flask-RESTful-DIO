import json
from typing import Tuple
from flask import Response, jsonify
from src.models.Cliente import Cliente

class ClienteService:
    def listar_clientes(self) -> Tuple[Response, int]:
        clientes = Cliente.query.all()
        return jsonify(clientes), 200


    def adicionar_cliente(self, dados) -> Tuple[Response, int]:
        dados = json.loads(dados)
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
                return jsonify({'success': 'Cliente criado com sucesso!', 'objeto': cliente}), 201
            except:
                return jsonify({'error': 'Aconteceu um erro ao salvar o registro'}), 500
        return jsonify({'error': 'Estão faltando campos no JSON'}), 400


    def modificar_cliente(self, dados) -> Tuple[Response, int]:
        dados = json.loads(dados)
        try:
            cliente = Cliente.query.filter_by(cpf=dados['cpf']).first()
        except:
            return jsonify({'error': 'CPF não informado'}), 400

        if 'nome' in dados:
            cliente.nome = dados['nome']
        if 'endereco' in dados:
            cliente.endereco = dados['endereco']
        if 'clubeBeneficios' in dados:
            cliente.clubeBeneficios = dados['clubeBeneficios']
        cliente.salvar()
        return jsonify({'success': 'Registro alterado com sucesso', 'objeto': cliente}), 200


    def remover_cliente(self, dados) -> Tuple[Response, int]:
        dados = json.loads(dados)
        try:
            cliente = Cliente.query.filter_by(cpf=dados['cpf']).first()
        except:
            return jsonify({'error': 'Registro não encontrado'}), 404

        cliente.apagar()
        return jsonify({'success': 'Registro apagado'}), 200

