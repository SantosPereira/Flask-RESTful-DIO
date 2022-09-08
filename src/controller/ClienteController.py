from flask import request, make_response
from flask_restful import Resource
from src.service.ClienteService import ClienteService
from src.util.Auth import auth


class ClienteController(Resource):
    def __init__(self) -> None:
        super().__init__()


    @auth.login_required
    def get(self):
        resposta, status = ClienteService.listar_clientes(self)
        return make_response(resposta, status)


    @auth.login_required
    def post(self):
        resposta, status = ClienteService.adicionar_cliente(self, request.data)
        return make_response(resposta, status)


    @auth.login_required
    def put(self):
        resposta, status = ClienteService.modificar_cliente(self, request.data)
        return make_response(resposta, status)


    @auth.login_required
    def delete(self):
        resposta, status = ClienteService.remover_cliente(self, request.data)
        return make_response(resposta, status)
