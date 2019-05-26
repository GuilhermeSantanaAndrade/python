from flask import Blueprint, jsonify, request
from infra.validacao import validar_campos
from infra.to_dict import to_dict, to_dict_list
from services.disciplina_service import \
    listar as service_listar, \
    localizar as service_localizar, \
    criar as service_criar, \
    remover as service_remover, \
    atualizar as service_atualizar, \
    DisciplinaJaExiste, \
    CoordenadorNaoExiste,\
    StatusInvalido


disciplina_app = Blueprint('disciplina_app', __name__, template_folder='templates')

campos = ["id", "nome", "status", "plano_ensino", "carga_horaria", "id_coordenador"]
tipos = [int, str, int, str,int , int]

@disciplina_app.route('/disciplina', methods=['GET'])
def listar():
    lista = service_listar()
    return jsonify(to_dict_list(lista))

@disciplina_app.route('/disciplina/<int:id>', methods=['GET'])
def localizar(id):
    x = service_localizar(id)
    if x != None:
        return jsonify(to_dict(x))
    return '', 404

@disciplina_app.route('/disciplina', methods=['POST'])
def criar():
    dados = request.get_json()
    print(dados)
    if not validar_campos(dados, campos, tipos):
        return '', 422
    try:
        #criado = service_criar(dados['id'], dados['id_disciplina'], dados['id_professor'] ...)
        criado = service_criar(**dados)
        return jsonify(to_dict(criado))
    except DisciplinaJaExiste:
        return 'Disciplina ja existe', 409
    except CoordenadorNaoExiste:
        return 'Coordenador não existe', 404
    except StatusInvalido:
        return 'Status invalido', 422

@disciplina_app.route('/disciplina/<int:id>', methods=['DELETE'])
def remover(id):
    removido = service_remover(id)
    if removido != None:
        return jsonify(to_dict(removido))
    return '', 404

@disciplina_app.route('/disciplina/<int:id>', methods=['PUT'])
def atualizar(id):
    dados = request.get_json()
    if not validar_campos(dados, campos, tipos):
        return '', 422
    try:
        #atualizado = service_atualizar(id, dados['id'], dados['nome'])
        dados['id_antigo'] = id
        dados['id_novo'] = dados['id']
        del dados['id']
        atualizado = service_atualizar(**dados)
    except DisciplinaJaExiste:
        return 'Disciplina ja existe', 409
    except StatusInvalido:
        return 'Status invalido', 422
    except CoordenadorNaoExiste:
        return 'Coordenador não existe', 404
    if atualizado != None:
        return jsonify(to_dict(atualizado))
    return '', 404