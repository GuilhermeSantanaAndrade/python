from flask import Blueprint, jsonify, request
from infra.validacao import validar_campos
from infra.to_dict import to_dict, to_dict_list
from services.solicitacao_matricula_service import \
    listar as service_listar, \
    localizar as service_localizar, \
    criar as service_criar, \
    remover as service_remover, \
    atualizar as service_atualizar, \
    Solicitacao_matriculaJaExiste

solicitacao_matriculas_app = Blueprint('solicitacao_matriculas_app', __name__, template_folder='templates')

campos = ["id", "id_aluno", "id_disciplina_ofertada", "dt_solicitacao", "id_coordenador", "status"]
tipos = [int, int, int,str,int,int] 

@solicitacao_matriculas_app.route('/solicitacao_matriculas', methods=['GET'])
def listar():
    lista = service_listar()
    return jsonify(to_dict_list(lista))

@solicitacao_matriculas_app.route('/solicitacao_matriculas/<int:id>', methods=['GET'])
def localizar(id):
    x = service_localizar(id)
    if x != None:
        return jsonify(to_dict(x))
    return '', 404

@solicitacao_matriculas_app.route('/solicitacao_matriculas', methods=['POST'])
def criar():
    dados = request.get_json()
    print(dados)
    if not validar_campos(dados, campos, tipos):
        return '', 422
    try:
        criado = service_criar(dados['id'], dados['id_aluno'], dados['id_disciplina_ofertada'], dados['dt_solicitacao'], dados['id_coordenador'], dados['status'])
        return jsonify(to_dict(criado))
    except Solicitacao_matriculaJaExiste:
        return '', 409

@solicitacao_matriculas_app.route('/solicitacao_matricula/<int:id>', methods=['DELETE'])
def remover(id):
    removido = service_remover(id)
    if removido != None:
        return jsonify(to_dict(removido))
    return '', 404

@solicitacao_matriculas_app.route('/solicitacao_matriculas/<int:id>', methods=['PUT'])
def atualizar(id):
    dados = request.get_json()
    if not validar_campos(dados, campos, tipos):
        return '', 422
    try:
        atualizado = service_atualizar(id, dados['id'], dados['id_aluno'], dados['id_disciplina_ofertada'], dados['dt_solicitacao'], dados['id_coordenador'], dados['status'])
    except Solicitacao_matriculaJaExiste:
        return '', 409
    if atualizado != None:
        return jsonify(to_dict(atualizado))
    return '', 404