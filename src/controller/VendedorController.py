from flask import request, make_response
from flask_restful import Resource
from src.util.Auth import auth
from src.service.VendedorService import VendedorService

class VendedorController(Resource):
    def __init__(self) -> None:
        super().__init__()

    @auth.login_required
    def get(self):
        return make_response(VendedorService.listar_vendedores(self))

    @auth.login_required
    def post(self):
        return make_response(VendedorService.salvar_vendedor(self, request.data))

    @auth.login_required
    def put(self):
        return make_response(VendedorService.modificar_vendedor(self, request.data))

    @auth.login_required
    def delete(self):
        return make_response(VendedorService.apagar_vendedor(self, request.data))
