from flask import Blueprint, jsonify, request
coordenador_app = Blueprint('coordenador_app', __name__, template_folder='templates')
coordenador_db = []

@coordenador_app.route('/coordenador', methods=['GET'])
def listar():
    return jsonify(coordenador_db)

@coordenador_app.route('/coordenador/<int:id>', methods=['GET'])
def localizar(id):
    for coordenador in coordenador_db:
        if coordenador['id'] == id:
            return jsonify(coordenador)
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


@coordenador_app.route('/coordenador', methods=['POST'])
def criar():
    dados = request.get_json()
    if not validar_campos(dados,campo,tipo):
        return 'ERRO NOS PARAMETROS'
    coordenador_db.append(dados)
    return jsonify(dados)


@coordenador_app.route('/coordenador/<int:id>', methods=['DELETE'])
def remover(id):
    index = 0
    for coordenador in coordenador_db:
        if coordenador['id'] == id:
            del coordenador_db[index]
            return jsonify(coordenador)
        index += 1
    return '', 404

@coordenador_app.route('/coordenador/<int:id>', methods=['PUT'])
def atualizar(id):
    dados = request.get_json()
    index = 0
    for coordenador in coordenador_db:
        if coordenador['id'] == id:
            coordenador['id'] = dados['id']
            coordenador['nome'] = dados['nome']
            return jsonify(coordenador)
        index += 1
    return '', 404