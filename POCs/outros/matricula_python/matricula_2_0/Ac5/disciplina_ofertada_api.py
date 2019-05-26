from flask import Blueprint, jsonify, request
disciplina_ofertada_app = Blueprint('disciplina_ofertada_app', __name__, template_folder='templates')
disciplina_ofertada_db = []

@disciplina_ofertada_app.route('/disciplina_ofertada', methods=['GET'])
def listar():
    return jsonify(disciplina_ofertada_db)

@disciplina_ofertada_app.route('/disciplina_ofertada/<int:id>', methods=['GET'])
def localizar(id):
    for disciplina_ofertada in disciplina_ofertada_db:
        if disciplina_ofertada['id'] == id:
            return jsonify(disciplina_ofertada)
    return '', 404


def comparar_duplicacao_campos(a, b):
    return a['id_disciplina'] == b['id_disciplina'] and \
            a['ano'] == b['ano'] and \
            a['semestre'] == b['semestre'] and \
            a['turma'] == b['turma'] and \
            a['id_curso'] == b['id_curso']

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
campo = ["id","id_disciplina","id_professor","ano","semestre","turma","id_curso","data"]
tipo = [int,int,int,int,int,str,int,str]



@disciplina_ofertada_app.route('/disciplina_ofertada', methods=['POST'])
def criar():
    dados = request.get_json()
    if not validar_campos(dados,campo,tipo):
        return 'ERRO NOS PARAMETROS', 422
    for disc in disciplina_ofertada_db:
        if comparar_duplicacao_campos(disc, dados):
            return 'erro nos parametros', 409
    disciplina_ofertada_db.append(dados)
    return jsonify(dados)

@disciplina_ofertada_app.route('/disciplina_ofertada/<int:id>', methods=['DELETE'])
def remover(id):
    index = 0
    for disciplina_ofertada in disciplina_ofertada_db:
        if disciplina_ofertada['id'] == id:
            del disciplina_ofertada_db[index]
            return jsonify(disciplina_ofertada)
        index += 1
    return '', 404

@disciplina_ofertada_app.route('/disciplina_ofertada/<int:id>', methods=['PUT'])
def atualizar(id):
    dados = request.get_json()
    index = 0
    for disciplina_ofertada in disciplina_ofertada_db:
        if disciplina_ofertada['id'] == id:
            disciplina_ofertada['id'] = dados['id']
            disciplina_ofertada['id_disciplina'] = dados['id_disciplina']
            disciplina_ofertada['id_professor'] = dados['id_professor']
            disciplina_ofertada['ano'] = dados['ano']
            disciplina_ofertada['semestre'] = dados['semestre']
            disciplina_ofertada['turma'] = dados['turma']
            disciplina_ofertada['id_curso'] = dados ['id_curso']
            disciplina_ofertada['data'] = dados['data']
            return jsonify(disciplina_ofertada)
        index += 1
    return '', 404

