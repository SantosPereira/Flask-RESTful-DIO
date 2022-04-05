import unittest
import requests
from src.controller.UsuarioController import UsuarioController
from src.models.Usuario import Usuario

# usuário qualquer
USUARIO = Usuario.query.all()[0]


class UsuarioControllerTest(unittest.TestCase):
    def test_cadastrar_usuario(self):
        resposta = requests.post(url="http://127.0.0.1:5000/api/usuario",data={"login":"teste1","senha":"senha12"})
        requests.delete(url="http://127.0.0.1:5000/api/usuario",headers={"Authorization":"teste senha12"})
        self.assertEqual(resposta.status_code, 201)
    