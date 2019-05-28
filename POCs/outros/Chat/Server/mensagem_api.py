from flask import Blueprint, jsonify, request
from infra.validacao import validar_campos
from infra.to_dict import to_dict, to_dict_list
from datetime import datetime
from services.mensagem_service import \
    listar as service_listar, \
    localizarRange as service_localizar, \
    criar as service_criar, \
    remover as service_remover, \
    atualizar as service_atualizar, \
    MensagemJaExiste, UsuarioNaoExiste, SegredoInvalido

mensagens_app = Blueprint('mensagens_app', __name__, template_folder='templates')

campos = ["id", "id_remetente", "id_destinatario", "data_hora", "texto"]
tipos = [int, int, int, str, str]

@mensagens_app.route('/msg', methods=['POST'])
def criar():
    dados = request.get_json()
    campos = ["de", "para", "segredo", "texto"]
    tipos = [int, int, str, str]

    if not validar_campos(dados, campos, tipos):
        return '', 422
    try:
        criado = service_criar(dados['segredo'], dados['de'], dados['para'], dados['texto'])
        return jsonify(to_dict(criado))
    except MensagemJaExiste:
        return 'Id de Mensagem já cadastrado', 409
    except UsuarioNaoExiste:
        return UsuarioNaoExiste, 404
    except SegredoInvalido:
        return 'Segredo inválido', 403

@mensagens_app.route('/msg', methods=['GET'])
def listar():
    lista = service_listar()
    return jsonify(to_dict_list(lista))

@mensagens_app.route('/msg/<int:id>', methods=['GET'])
def localizar(id):  
    inicio = None
    fim = None
    segredo = None
    try:
        segredo = str(request.args.get('segredo'))
    except:
        pass

    try:
        inicio = int(request.args.get('inicio'))
    except:
        inicio = 0
    
    try:
        fim = int(request.args.get('fim'))
    except:
        fim = inicio

    try:
        x = service_localizar(id, segredo, inicio, fim)
    except UsuarioNaoExiste:
        return UsuarioNaoExiste, 404
    except SegredoInvalido:
        return 'Segredo inválido', 403

    if x != None:
        return jsonify(to_dict(x))
    return '', 404

@mensagens_app.route('/msg/<int:id>', methods=['PUT'])
def atualizar(id):
    dados = request.get_json()
    if not validar_campos(dados, campos, tipos):
        return '', 422
    try:
        atualizado = service_atualizar(id, dados['id'], dados['id_remetente'], dados['id_destinatario'], dados['data_hora'], dados['texto'])
    except MensagemJaExiste:
        return 'id de mensagem ja cadastrado', 409
    if atualizado != None:
        return jsonify(to_dict(atualizado))
    return '', 404

@mensagens_app.route('/msg/<int:id>', methods=['DELETE'])
def remover(id):
    try:
        removido = service_remover(id)
    except:
        return 'Erro ao remover', 422
    if removido != None:
        return jsonify(to_dict(removido))
    return '', 404