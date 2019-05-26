from flask import Blueprint, jsonify, request
professores_app = Blueprint('professores_app', __name__, template_folder='templates')
professores_db = []

@professores_app.route('/professores', methods=['GET'])
def listar():
    return jsonify(professores_db)

@professores_app.route('/professores/<int:id>', methods=['GET'])
def localizar(id):
    for professor in professores_db:
        if professor['id'] == id:
            return jsonify(professor)
    return '', 404

def validar_campos(obj, campos, tipos):
    if type(obj) != dict:
        return False
    for k in obj:
        if k not in campos:
            return False
    for k in campos:
        if k not in obj:
            return False
    t = []
    for item in campos:
        t.append(type(obj[item]))
    if t != tipos:
        return False
    return True

campo = ["id","nome"]
tipo = [int,str]

@professores_app.route('/professores', methods=['POST'])
def criar():
    dados = request.get_json()
    if not validar_campos(dados,campo,tipo):
        return 'ERRO NOS PARAMETROS' , 422
    professores_db.append(dados)
    return jsonify(dados)


@professores_app.route('/professores/<int:id>', methods=['DELETE'])
def remover(id):
    index = 0
    for professor in professores_db:
        if professor['id'] == id:
            del professores_db[index]
            return jsonify(professor)
        index += 1
    return '', 404

@professores_app.route('/professores/<int:id>', methods=['PUT'])
def atualizar(id):
    dados = request.get_json()
    index = 0
    for professor in professores_db:
        if professor['id'] == id:
            professor['id'] = dados['id']
            professor['nome'] = dados['nome']
            return jsonify(professor)
        index += 1
    return '', 404