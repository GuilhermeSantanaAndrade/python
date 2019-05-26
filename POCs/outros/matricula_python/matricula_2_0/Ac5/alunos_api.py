from flask import Blueprint, jsonify, request
alunos_app = Blueprint('alunos_app', __name__, template_folder='templates')
alunos_db = []

@alunos_app.route('/alunos', methods=['GET'])
def listar():
    return jsonify(alunos_db)

@alunos_app.route('/alunos/<int:id>', methods=['GET'])
def localizar(id):
    for aluno in alunos_db:
        if aluno['id'] == id:
            return jsonify(aluno)
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

@alunos_app.route('/alunos', methods=['POST'])
def criar():
    dados = request.get_json()
    if not validar_campos(dados,campo,tipo):
        return 'ERRO NOS PARAMETROS', 422
    alunos_db.append(dados)
    return jsonify(dados)


@alunos_app.route('/alunos/<int:id>', methods=['DELETE'])
def remover(id):
    index = 0
    for aluno in alunos_db:
        if aluno['id'] == id:
            del alunos_db[index]
            return jsonify(aluno)
        index += 1
    return '', 404

@alunos_app.route('/alunos/<int:id>', methods=['PUT'])
def atualizar(id):
    dados = request.get_json()
    index = 0
    for aluno in alunos_db:
        if aluno['id'] == id:
            aluno['id'] = dados['id']
            aluno['nome'] = dados['nome']
            return jsonify(aluno)
        index += 1
    return '', 404