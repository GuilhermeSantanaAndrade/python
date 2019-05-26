from flask import Blueprint, jsonify, request
from infra.validacao import validar_campos
from infra.to_dict import to_dict, to_dict_list
from services.alunos_service import \
    listar as service_listar, \
    localizar as service_localizar, \
    criar as service_criar, \
    remover as service_remover, \
    atualizar as service_atualizar, \
    AlunoJaExiste
from solicitacao_matricula_api import solicitacao_matriculas_app

alunos_app = Blueprint('alunos_app', __name__, template_folder='templates')

campos = ["id", "nome"]
tipos = [int, str]

@alunos_app.route('/alunos', methods=['GET'])
def listar():
    lista = service_listar()
    return jsonify(to_dict_list(lista))

@alunos_app.route('/alunos/<int:id>', methods=['GET'])
def localizar(id):
    x = service_localizar(id)
    if x != None:
        return jsonify(to_dict(x))
    return '', 404

@alunos_app.route('/alunos', methods=['POST'])
def criar():
    dados = request.get_json()
    print(dados)
    if not validar_campos(dados, campos, tipos):
        return '', 422
    try:
        criado = service_criar(dados['id'], dados['nome'])
        return jsonify(to_dict(criado))
    except AlunoJaExiste:
        return 'Aluno ja cadastrado', 409

@alunos_app.route('/alunos/<int:id>', methods=['PUT'])
def atualizar(id):
    dados = request.get_json()
    if not validar_campos(dados, campos, tipos):
        return '', 422
    try:
        atualizado = service_atualizar(id, dados['id'], dados['nome'])
    except AlunoJaExiste:
        return 'Aluno ja cadastrado', 409
    if atualizado != None:
        return jsonify(to_dict(atualizado))
    return '', 404

@alunos_app.route('/alunos/<int:id>', methods=['DELETE'])
def remover(id):
    from services.solicitacao_matricula_service import listar as listar_solicitacao_matriculas
    solicitacao_matriculas = to_dict_list(listar_solicitacao_matriculas())
    for solicitacao in solicitacao_matriculas:
        if solicitacao['id_aluno'] == id:
            return 'Aluno já foi atrelado a uma ou mais matérias. Exclusão não permitida.', 409
        
    removido = service_remover(id)
    if removido != None:
        return jsonify(to_dict(removido))
    return '', 404