from flask import Blueprint, jsonify, request
from infra.to_dict import to_dict, to_dict_list
from disciplina_ofertada_api import listar as listar_disciplina_ofertada
from services.solicitacao_matricula_service import \
    listar as service_listar, \
    

alunos_matriculados_app = Blueprint('relatorio', __name__, template_folder='templates')


@alunos_matriculados_app.route('/relatorio', methods=['GET'])
def listar():
    lista = (listar_alunos[1],
    return jsonify(to_dict_list(lista))

