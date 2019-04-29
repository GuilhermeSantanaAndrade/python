from flask import Blueprint, jsonify, request
from infra.validacao import validar_campos
from infra.to_dict import to_dict, to_dict_list
from services.disciplina_ofertada_service import \
    listar as service_listar, \
    localizar as service_localizar, \
    criar as service_criar, \
    remover as service_remover, \
    atualizar as service_atualizar, \
    Disciplina_ofertadaJaExiste

disciplina_ofertadas_app = Blueprint('disciplina_ofertadas_app', __name__, template_folder='templates')

campos = ["id","id_disciplina","id_professor","ano","semestre","turma","id_curso","data"]
tipos = [int,int,int,int,int,str,int,str]

@disciplina_ofertadas_app.route('/disciplina_ofertadas', methods=['GET'])
def listar():
    lista = service_listar()
    return jsonify(to_dict_list(lista))

@disciplina_ofertadas_app.route('/disciplina_ofertadas/<int:id>', methods=['GET'])
def localizar(id):
    x = service_localizar(id)
    if x != None:
        return jsonify(to_dict(x))
    return '', 404

@disciplina_ofertadas_app.route('/disciplina_ofertadas', methods=['POST'])
def criar():
    dados = request.get_json()
    print(dados)
    if not validar_campos(dados, campos, tipos):
        return '', 422
    
    try:
        criado = service_criar(dados['id'], dados['id_disciplina'], dados['id_professor'], dados['ano'], dados['semestre'], dados['turma'], dados['id_curso'], dados['data'])
        return jsonify(to_dict(criado))
    except Disciplina_ofertadaJaExiste:
        return '', 409

@disciplina_ofertadas_app.route('/disciplina_ofertadas/<int:id>', methods=['DELETE'])
def remover(id):
    removido = service_remover(id)
    if removido != None:
        return jsonify(to_dict(removido))
    return '', 404

@disciplina_ofertadas_app.route('/disciplina_ofertadas/<int:id>', methods=['PUT'])
def atualizar(id):
    dados = request.get_json()
    if not validar_campos(dados, campos, tipos):
        return '', 422
    try:
        atualizado = service_atualizar(id, dados['id'], dados['id_disciplina'], dados['id_professor'], dados['ano'], dados['semestre'], dados['turma'], dados['id_curso'], dados['data'])
    except Disciplina_ofertadaJaExiste:
        return '', 409
    if atualizado != None:
        return jsonify(to_dict(atualizado))
    return '', 404