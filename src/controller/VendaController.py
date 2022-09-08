from flask import request, make_response
from flask_restful import Resource
from src.util.Auth import auth
from src.service.VendaService import VendaService

class VendaController(Resource):
    def __init__(self) -> None:
        super().__init__()


    def get(self):
        resposta, status = VendaService.listar_vendas(self)
        return make_response(resposta, status)


    @auth.login_required
    def post(self):
        resposta, status = VendaService.adicionar_venda(self, request.data)
        return make_response(resposta, status)


    @auth.login_required
    def put(self):
        resposta, status = VendaService.modificar_venda(self, request.data)
        return make_response(resposta, status)

    @auth.login_required
    def delete(self):
        resposta, status = VendaService.remover_venda(self, request.data)
        return make_response(resposta, status)