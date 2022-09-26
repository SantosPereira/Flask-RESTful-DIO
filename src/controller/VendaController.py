from flask import request, make_response
from flask_restful import Resource
from src.util.Auth import auth
from src.service.VendaService import VendaService


class VendaController(Resource):
    def __init__(self) -> None:
        super().__init__()


    def get(self):
        return make_response(VendaService.listar_vendas(self))


    @auth.login_required
    def post(self):
        return make_response(VendaService.adicionar_venda(self, request.data))


    @auth.login_required
    def put(self):
        return make_response(VendaService.modificar_venda(self, request.data))


    @auth.login_required
    def delete(self):
        return make_response(VendaService.remover_venda(self, request.data))
