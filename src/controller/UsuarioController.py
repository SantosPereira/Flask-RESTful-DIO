from flask import request, make_response
from flask_restful import Resource
from src.util.Auth import auth
from src.service.UsuarioService import UsuarioService

class UsuarioController(Resource):
    def __init__(self) -> None:
        super().__init__()

    @auth.login_required
    def get(self):
        resposta, status = UsuarioService.listar_usuario(self)
        return make_response(resposta, status)

    def post(self):
        resposta, status = UsuarioService.salvar_usuario(self, request.data)
        return make_response(resposta, status)

    @auth.login_required
    def put(self):
        resposta, status = UsuarioService.modificar_usuario(self, request.data)
        return make_response(resposta, status)

    @auth.login_required
    def delete(self):
        resposta, status = UsuarioService.apagar_usuario(self, request.data)
        return make_response(resposta, status)