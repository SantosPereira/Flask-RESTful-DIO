import json
import unittest
import requests
from requests.auth import HTTPBasicAuth
from src.controller.UsuarioController import UsuarioController
from src.models.Usuario import Usuario

# usuário qualquer
USUARIO = Usuario.query.all()[0]
URL_BASE = "http://localhost:5000"

class UsuarioControllerTest(unittest.TestCase):
    def test_cadastrar_usuario(self):
        resposta = requests.post(url=f"{URL_BASE}/api/usuario/",json={"login":"teste1","senha":"senha12"})
        requests.delete(url=f"{URL_BASE}/api/usuario/", auth=HTTPBasicAuth('teste1', 'senha12'), json={"login":"teste1","senha":"senha12"})
        self.assertEqual(resposta.status_code, 201)
    
    def test_listar_usuario(self):
        resposta = requests.get(url=f"{URL_BASE}/api/usuario/", auth=HTTPBasicAuth('pedro', '1234'))
        self.assertEqual(resposta.status_code, 200)

    def test_modificar_usuario(self):
        resposta = requests.post(url=f"{URL_BASE}/api/usuario/",json={"login":"teste","senha":"senha12"})
        resposta = requests.put(url=f"{URL_BASE}/api/usuario/", auth=HTTPBasicAuth('pedro', '1234'), json={"login":"teste","senha":"senha15"})
        requests.delete(url=f"{URL_BASE}/api/usuario/", auth=HTTPBasicAuth('pedro', '1234'), json={"login":"teste","senha":"senha15"})
        self.assertEqual(resposta.status_code, 200)
        
    