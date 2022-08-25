import json
from flask import request, jsonify
from flask_restful import Resource
from src.util.Auth import auth
from src.models.Usuario import Usuario
from src.service.UsuarioService import UsuarioService

class UsuarioController(Resource):
    def __init__(self) -> None:
        super().__init__()

    @auth.login_required
    def get(self):
        return UsuarioService.listar_usuario(self)

    def post(self):
        return UsuarioService.salvar_usuario(self, request.data)

    @auth.login_required
    def put(self):
        return UsuarioService.modificar_usuario(self, request.data)

    @auth.login_required
    def delete(self):
        return UsuarioService.apagar_usuario(self, request.data)