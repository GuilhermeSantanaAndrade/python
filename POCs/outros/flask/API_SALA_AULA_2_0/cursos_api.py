from flask import Blueprint, jsonify, request
from infra.validacao import validar_campos
from infra.to_dict import to_dict, to_dict_list
from services.curso_service import \
    listar as service_listar, \
    localizar as service_localizar, \
    criar as service_criar, \
    remover as service_remover, \
    atualizar as service_atualizar, \
    CursoJaExiste

cursos_app = Blueprint('cursos_app', __name__, template_folder='templates')

campos = ["id", "nome"]
tipos = [int, str]

@cursos_app.route('/cursos', methods=['GET'])
def listar():
    lista = service_listar()
    return jsonify(to_dict_list(lista))

@cursos_app.route('/cursos/<int:id>', methods=['GET'])
def localizar(id):
    x = service_localizar(id)
    if x != None:
        return jsonify(to_dict(x))
    return '', 404

@cursos_app.route('/cursos', methods=['POST'])
def criar():
    dados = request.get_json()
    print(dados)
    if not validar_campos(dados, campos, tipos):
        return '', 422
    try:
        criado = service_criar(dados['id'], dados['nome'])
        return jsonify(to_dict(criado))
    except CursoJaExiste:
        return '', 409

@cursos_app.route('/cursos/<int:id>', methods=['DELETE'])
def remover(id):
    removido = service_remover(id)
    if removido != None:
        return jsonify(to_dict(removido))
    return '', 404

@cursos_app.route('/cursos/<int:id>', methods=['PUT'])
def atualizar(id):
    dados = request.get_json()
    if not validar_campos(dados, campos, tipos):
        return '', 422
    try:
        atualizado = service_atualizar(id, dados['id'], dados['nome'])
    except CursoJaExiste:
        return '', 409
    if atualizado != None:
        return jsonify(to_dict(atualizado))
    return '', 404