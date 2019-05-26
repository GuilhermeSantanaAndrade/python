from flask import Blueprint, jsonify, request
disciplina_app = Blueprint('disciplina_app', __name__, template_folder='templates')
disciplina_db = []

@disciplina_app.route('/disciplina', methods=['GET'])
def listar():
    return jsonify(disciplina_db)

@disciplina_app.route('/disciplina/<int:id>', methods=['GET'])
def localizar(id):
    for disciplina in disciplina_db:
        if disciplina['id'] == id:
            return jsonify(disciplina)
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

campo = ["id","nome","status","plano_ensino","carga_horaria","id_coordenador"]
tipo = [int,str,int,str,int,int]


@disciplina_app.route('/disciplina', methods=['POST'])
def criar():
    dados = request.get_json()
    if not validar_campos(dados,campo,tipo):
        return 'ERRO NOS PARAMETROS', 422
    if dados['status'] == 1 or dados ['status'] == 0:
        disciplina_db.append(dados)
        return jsonify(dados)
    return 'STATUS DEVE SER 1 OU 0', 404

@disciplina_app.route('/disciplina/<int:id>', methods=['DELETE'])
def remover(id):
    index = 0
    for disciplina in disciplina_db:
        if disciplina['id'] == id:
            del disciplina_db[index]
            return jsonify(disciplina)
        index += 1
    return '', 404

@disciplina_app.route('/disciplina/<int:id>', methods=['PUT'])
def atualizar(id):
    dados = request.get_json()
    index = 0
    for disciplina in disciplina_db:
        if disciplina['id'] == id:
            disciplina['id'] = dados['id']
            disciplina['nome'] = dados['nome']
            disciplina['status'] = dados['status']
            disciplina['plano_ensino'] = dados['plano_ensino']
            disciplina['carga_horaria'] = dados['carga_horaria']
            disciplina['id_coordenador'] = dados['id_coordenador']
            return jsonify(disciplina)
        index += 1
    return '', 404