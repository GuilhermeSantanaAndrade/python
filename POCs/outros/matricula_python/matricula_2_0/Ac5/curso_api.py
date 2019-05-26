from flask import Blueprint, jsonify, request
curso_app = Blueprint('curso_app', __name__, template_folder='templates')
curso_db = []

@curso_app.route('/curso', methods=['GET'])
def listar():
    return jsonify(curso_db)

@curso_app.route('/curso/<int:id>', methods=['GET'])
def localizar(id):
    for curso in curso_db:
        if curso['id'] == id:
            return jsonify(curso)
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

@curso_app.route('/curso', methods=['POST'])
def criar():
    dados = request.get_json()
    if not validar_campos(dados,campo,tipo):
        return 'ERRO NOS PARAMETROS', 422
    curso_db.append(dados)
    return jsonify(dados)


@curso_app.route('/curso/<int:id>', methods=['DELETE'])
def remover(id):
    index = 0
    for curso in curso_db:
        if curso['id'] == id:
            del curso_db[index]
            return jsonify(curso)
        index += 1
    return '', 404

@curso_app.route('/curso/<int:id>', methods=['PUT'])
def atualizar(id):
    dados = request.get_json()
    index = 0
    for curso in curso_db:
        if curso['id'] == id:
            curso['id'] = dados['id']
            curso['nome'] = dados['nome']
            return jsonify(curso)
        index += 1
    return '', 404