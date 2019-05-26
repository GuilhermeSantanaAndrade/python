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

@alunos_app.route('/alunos', methods=['POST'])
def criar():
    dados = request.get_json()
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