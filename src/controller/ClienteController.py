from flask import request, make_response
from flask_restful import Resource
from src.service.ClienteService import ClienteService
from src.util.Auth import auth


class ClienteController(Resource):
    def __init__(self) -> None:
        super().__init__()


    @auth.login_required
    def get(self):
        return make_response(ClienteService.listar_clientes(self))


    @auth.login_required
    def post(self):
        return make_response(ClienteService.adicionar_cliente(self, request.data))


    @auth.login_required
    def put(self):
        return make_response(ClienteService.modificar_cliente(self, request.data))


    @auth.login_required
    def delete(self):
        return make_response(ClienteService.remover_cliente(self, request.data))
