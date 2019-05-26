from flask import Blueprint, jsonify, request
from infra.validacao import validar_campos
from infra.to_dict import to_dict, to_dict_list
from services.disciplina_ofertada_service import \
    listar as service_listar, \
    localizar as service_localizar, \
    criar as service_criar, \
    remover as service_remover, \
    atualizar as service_atualizar, \
    DisciplinaOfertadaJaExiste, \
    ProfessorNaoExiste, \
    DataInvalida, \
    DisciplinaNaoExiste,\
    CursoNaoExiste

disciplina_ofertada_app = Blueprint('disciplina_ofertada_app', __name__, template_folder='templates')

campos = ["id", "id_disciplina", "id_professor", "ano", "semestre", "turma", "id_curso", "data"]
tipos = [int, int, int, int, int, str, int, str]

@disciplina_ofertada_app.route('/oferta', methods=['GET'])
def listar():
    lista = service_listar()
    return jsonify(to_dict_list(lista))

@disciplina_ofertada_app.route('/oferta/<int:id>', methods=['GET'])
def localizar(id):
    x = service_localizar(id)
    if x != None:
        return jsonify(to_dict(x))
    return '', 404

@disciplina_ofertada_app.route('/oferta', methods=['POST'])
def criar():
    dados = request.get_json()
    print(dados)
    if not validar_campos(dados, campos, tipos):
        return '', 422
    try:
        #criado = service_criar(dados['id'], dados['id_disciplina'], dados['id_professor'] ...)
        criado = service_criar(**dados)
        return jsonify(to_dict(criado))
    except DisciplinaOfertadaJaExiste:
        return 'Disciplina Ofertada ja existe', 409
    except DataInvalida:
        return 'Data invalida', 422
    except ProfessorNaoExiste:
        return 'Professor não existe', 404
    except DisciplinaNaoExiste:
        return 'Disciplina não existe', 404
    except CursoNaoExiste:
        return 'Curso não existe', 404

@disciplina_ofertada_app.route('/oferta/<int:id>', methods=['DELETE'])
def remover(id):
    removido = service_remover(id)
    if removido != None:
        return jsonify(to_dict(removido))
    return '', 404

@disciplina_ofertada_app.route('/oferta/<int:id>', methods=['PUT'])
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
    except DisciplinaOfertadaJaExiste:
        return 'Disciplina Ofertada ja existe', 409
    except ProfessorNaoExiste:
        return 'Professor não existe', 404
    except DataInvalida:
        return 'Data invalida', 422
    except DisciplinaNaoExiste:
        return 'Disciplina não existe', 422
    except CursoNaoExiste:
        return 'Curso não existe', 422
    if atualizado != None:
        return jsonify(to_dict(atualizado))
    return '', 404