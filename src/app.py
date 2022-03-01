from flask import Flask
from flask_restful import Api
from controller.VeiculoController import VeiculoController
from controller.FinanceiroController import FinanceiroController
from controller.LojaController import LojaController
from controller.UsuarioController import UsuarioController
from controller.VendaController import VendaController

app = Flask(__name__)
api = Api(app)

api.add_resource(VeiculoController, '/api/veiculo/')
api.add_resource(FinanceiroController, '/api/financeiro/')
api.add_resource(LojaController, '/api/loja/')
api.add_resource(UsuarioController, '/api/usuario/')
api.add_resource(VendaController, '/api/venda/')

if __name__ == '__main__':
    app.run(debug=True)
