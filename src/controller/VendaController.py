import json
from flask import request
from flask_restful import Resource


class Venda(Resource):
    def __init__(self) -> None:
        super().__init__()

    def get(self):
        return ''

    def post(self):
        dados = json.loads(request.data)
        return ''

    def put(self):
        return ''

    def delete(self):
        return ''
