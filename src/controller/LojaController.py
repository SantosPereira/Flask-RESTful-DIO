from flask import request, make_response
from flask_restful import Resource
from src.service.LojaService import LojaService


class LojaController(Resource):
    def __init__(self) -> None:
        super().__init__()

    def get(self):
        return make_response(LojaService.listar_lojas(self))

    def post(self):
        return make_response(LojaService.adicionar_loja(self, request.data))

    def put(self):
        return make_response(LojaService.modificar_loja(self, request.data))

    def delete(self):
        return make_response(LojaService.remover_loja(self, request.data))
