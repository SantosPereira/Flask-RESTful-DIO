from flask import Flask
from flask_restful import Api
from controller.VeiculoController import VeiculoController
from controller.FinanceiroController import FinanceiroController
from controller.LojaController import LojaController
from controller.UsuarioController import UsuarioController
from controller.VendaController import VendaController
from controller.VendedorController import VendedorController
from controller.ClienteController import ClienteController

app = Flask(__name__)
api = Api(app)

api.add_resource(VeiculoController, '/api/veiculo/')
api.add_resource(FinanceiroController, '/api/financeiro/')
api.add_resource(LojaController, '/api/loja/')
api.add_resource(UsuarioController, '/api/usuario/')
api.add_resource(VendaController, '/api/venda/')
api.add_resource(VendedorController, '/api/vendedor/')
api.add_resource(ClienteController, '/api/cliente/')

if __name__ == '__main__':
    app.run(debug=True)
