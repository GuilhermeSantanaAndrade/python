from flask import Blueprint, jsonify, request
from infra.validacao import validar_campos
from infra.to_dict import to_dict, to_dict_list
from services.usuario_service import \
    listar as service_listar, \
    listarParaFora as service_listarParaFora, \
    localizar as service_localizar, \
    criar as service_criar, \
    remover as service_remover, \
    atualizar as service_atualizar, \
    UsuarioJaExiste, \
    UsuarioComDependencia

usuarios_app = Blueprint('usuarios_app', __name__, template_folder='templates')

campos = ["id", "nome", "segredo"]
tipos = [int, str, str]

@usuarios_app.route('/usr', methods=['GET'])
def listarParaFora():
    lista = service_listarParaFora()
    return jsonify(to_dict(lista))

def listar():
    lista = service_listar()
    return jsonify(to_dict_list(lista))

@usuarios_app.route('/usr/<int:id>', methods=['GET'])
def localizar(id):
    x = service_localizar(id)
    if x != None:
        return jsonify(to_dict(x))
    return '', 404

@usuarios_app.route('/usr', methods=['POST'])
def criar():
    dados = request.get_json()
    campos = ["nome"]
    tipos = [str]

    if not validar_campos(dados, campos, tipos):
        return '', 422
    try:
        criado = service_criar(dados['nome'])
        return jsonify(to_dict(criado))
    except UsuarioJaExiste:
        return 'Usuário ja cadastrado', 409

@usuarios_app.route('/usr/<int:id>', methods=['PUT'])
def atualizar(id):
    dados = request.get_json()
    if not validar_campos(dados, campos, tipos):
        return '', 422
    try:
        atualizado = service_atualizar(id, dados['id'], dados['nome'], dados['segredo'])
    except UsuarioJaExiste:
        return 'Usuário ja cadastrado', 409
    if atualizado != None:
        return jsonify(to_dict(atualizado))
    return '', 404

@usuarios_app.route('/usr/<int:id>', methods=['DELETE'])
def remover(id):
    try:
        removido = service_remover(id)
    except UsuarioComDependencia:
        return 'Aluno possui mensagens vinculadas', 422
    if removido != None:
        return jsonify(to_dict(removido))
    return '', 404


