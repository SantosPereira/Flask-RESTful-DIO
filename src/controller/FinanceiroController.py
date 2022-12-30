from flask import request, make_response
from flask_restful import Resource
from src.service.FinanceiroService import FinanceiroService
from src.util.Auth import auth


class FinanceiroController(Resource):
    def __init__(self) -> None:
        super().__init__()

    def get(self):
        return make_response(FinanceiroService.listar_financeiros(self))

    def post(self):
        return make_response(FinanceiroService.adicionar_financeiro(self, request.data))

    def put(self):
        return make_response(FinanceiroService.modificar_financeiro(self, request.data))

    def delete(self):
        return make_response(FinanceiroService.remover_financeiro(self, request.data))
