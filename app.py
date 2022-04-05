from flask import Flask
from flask_restful import Api
from src.controller.VeiculoController import VeiculoController
from src.controller.FinanceiroController import FinanceiroController
from src.controller.LojaController import LojaController
from src.controller.UsuarioController import UsuarioController
from src.controller.VendaController import VendaController
from src.controller.VendedorController import VendedorController
from src.controller.ClienteController import ClienteController

app = Flask(__name__)
api = Api(app)

# api.add_resource(ApiController, '/api/')
api.add_resource(VeiculoController, '/api/veiculo/')
api.add_resource(FinanceiroController, '/api/financeiro/')
api.add_resource(LojaController, '/api/loja/')
api.add_resource(UsuarioController, '/api/usuario/')
api.add_resource(VendaController, '/api/venda/')
api.add_resource(VendedorController, '/api/vendedor/')
api.add_resource(ClienteController, '/api/cliente/')

if __name__ == '__main__':
    app.run(debug=True)
