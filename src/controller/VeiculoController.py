from flask import request, make_response
from flask_restful import Resource
from src.util.Auth import auth
from src.service.VeiculoService import VeiculoService


class VeiculoController(Resource):
    def __init__(self) -> None:
        super().__init__()

    def get(self):
        return make_response(VeiculoService.listar_veiculos(self))

    @auth.login_required
    def post(self):
        return make_response(VeiculoService.adcionar_veiculo(self, request.data))

    @auth.login_required
    def put(self):
        return make_response(VeiculoService.modificar_veiculo(self, request.data))

    @auth.login_required
    def delete(self):
        return make_response(VeiculoService.apagar_veiculo(self, request.data))
