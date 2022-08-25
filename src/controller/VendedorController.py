from flask import request
from flask_restful import Resource
from src.util.Auth import auth
from src.service.VendedorService import VendedorService

class VendedorController(Resource):
    def __init__(self) -> None:
        super().__init__()

    @auth.login_required
    def get(self):
        return VendedorService.listar_vendedores(self)

    @auth.login_required
    def post(self):
        return VendedorService.salvar_vendedor(self, request.data)

    @auth.login_required
    def put(self):
        return VendedorService.modificar_vendedor(self, request.data)

    @auth.login_required
    def delete(self):
        return VendedorService.apagar_vendedor(self, request.data)
