from flask import Blueprint, jsonify, request
solicitacao_matricula_app = Blueprint('solicitacao_matricula_app', __name__, template_folder='templates')
solicitacao_matricula_db = []

@solicitacao_matricula_app.route('/solicitacao_matricula', methods=['GET'])
def listar():
    return jsonify(solicitacao_matricula_db)

@solicitacao_matricula_app.route('/solicitacao_matricula/<int:id>', methods=['GET'])
def localizar(id):
    for solicitacao_matricula in solicitacao_matricula_db:
        if solicitacao_matricula['id'] == id:
            return jsonify(solicitacao_matricula)
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

campos = ["id", "id_aluno", "id_disciplina_ofertada","dt_solicitacao","id_coordenador","status"]
tipos = [int, int, int,str,int,int] 

@solicitacao_matricula_app.route('/solicitacao_matricula', methods=['POST'])
def criar():
    dados = request.get_json()
    if not validar_campos(dados, campos, tipos):
        return 'ERRO NOS PARAMETROS', 422
    if dados['status'] >= 1 and dados['status'] <=6:
        solicitacao_matricula_db.append(dados)
        return jsonify(dados)
    return 'Status invalido', 422


@solicitacao_matricula_app.route('/solicitacao_matricula/<int:id>', methods=['DELETE'])
def remover(id):
    index = 0
    for solicitacao_matricula in solicitacao_matricula_db:
        if solicitacao_matricula['id'] == id:
            del solicitacao_matricula_db[index]
            return jsonify(solicitacao_matricula)
        index += 1
    return '', 404

@solicitacao_matricula_app.route('/solicitacao_matricula/<int:id>', methods=['PUT'])
def atualizar(id):
    dados = request.get_json()
    index = 0
    for solicitacao_matricula in solicitacao_matricula_db:
        if solicitacao_matricula['id'] == id:
            solicitacao_matricula['id'] = dados['id']
            solicitacao_matricula['id_aluno'] = dados['id_aluno']
            solicitacao_matricula['id_disciplina_ofertada'] = dados['id_disciplina_ofertada']
            solicitacao_matricula['dt_solicitacao'] = dados['dt_solicitacao']
            solicitacao_matricula['id_coordenador'] = dados['id_coordenador']
            solicitacao_matricula['status'] = dados['status']
            return jsonify(solicitacao_matricula)
        index += 1
    return '', 404