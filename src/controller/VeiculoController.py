from flask import request, make_response
from flask_restful import Resource
from src.util.Auth import auth
from src.service.VeiculoService import VeiculoService


class VeiculoController(Resource):
    def __init__(self) -> None:
        super().__init__()

    def get(self):
        resposta, status = VeiculoService.listar_veiculos(self)
        return make_response(resposta, status)

    @auth.login_required
    def post(self):
        resposta, status = VeiculoService.adcionar_veiculo(self, request.data)
        return make_response(resposta, status)


    @auth.login_required
    def put(self):
        resposta, status = VeiculoService.modificar_veiculo(self, request.data)
        return make_response(resposta, status)


    @auth.login_required
    def delete(self):
        resposta, status = VeiculoService.apagar_veiculo(self, request.data)
        return make_response(resposta, status)
