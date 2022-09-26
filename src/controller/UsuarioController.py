from flask import request, make_response
from flask_restful import Resource
from src.util.Auth import auth
from src.service.UsuarioService import UsuarioService


class UsuarioController(Resource):
    def __init__(self) -> None:
        super().__init__()

    @auth.login_required
    def get(self):
        return make_response(UsuarioService.listar_usuario(self))

    def post(self):
        return make_response(UsuarioService.salvar_usuario(self, request.data))

    @auth.login_required
    def put(self):
        return make_response(UsuarioService.modificar_usuario(self, request.data))

    @auth.login_required
    def delete(self):
        return make_response(UsuarioService.apagar_usuario(self, request.data))
