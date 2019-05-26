from flask import Flask, jsonify, request
from alunos_api import alunos_app
from professores_api import professores_app
from disciplina_ofertada_api import disciplina_ofertada_app
from coordenador_api import coordenador_app
from curso_api import curso_app
from disciplina_api import disciplina_app
from solicitacao_matricula_api import solicitacao_matriculas_app
from infra.to_dict import to_dict_list

app = Flask(__name__)
app.register_blueprint(alunos_app)
app.register_blueprint(professores_app)
app.register_blueprint(disciplina_ofertada_app)
app.register_blueprint(coordenador_app)
app.register_blueprint(curso_app)
app.register_blueprint(disciplina_app)
app.register_blueprint(solicitacao_matriculas_app)


@app.route('/')
def all():
    from services.professores_service import listar as listar_professores
    from services.disciplina_ofertada_service import listar as listar_disciplinas_ofertadas
    from services.alunos_service import listar as listar_alunos
    from services.coordenador_service import listar as listar_coordenador
    from services.curso_service import listar as listar_curso
    from services.disciplina_service import listar as listar_disciplina
    from services.solicitacao_matricula_service import listar as listar_solicitacao_matricula
    database = {
        "ALUNOS": to_dict_list(listar_alunos()),
        "PROFESSORES": to_dict_list(listar_professores()),
        "COORDENADOR": to_dict_list(listar_coordenador()),
        "CURSO": to_dict_list(listar_curso()),
        "DISCIPLINAS_OFERTADAS": to_dict_list(listar_disciplinas_ofertadas()),
        "DISCIPLINAS": to_dict_list(listar_disciplina()),
        "SOLICITACAO_MATRICULA": to_dict_list(listar_solicitacao_matricula())
    }
    return jsonify(database)


@app.route('/relatorio')
def report():
    from services.professores_service import localizar as localizar_professor
    from services.alunos_service import localizar as localizar_aluno
    #from services.coordenador_service import listar as listar_coordenadores
    #from services.curso_service import listar as listar_cursos
    from services.disciplina_service import localizar as localizar_disciplina
    from services.disciplina_ofertada_service import localizar as localizar_disciplina_ofertada
    from services.solicitacao_matricula_service import listar as listar_solicitacao_matriculas

    solicitacao_matriculas = to_dict_list(listar_solicitacao_matriculas())

    relatorio = []
    for solicitacao in solicitacao_matriculas:
        item = {}
        aluno = localizar_aluno(solicitacao['id_aluno'])        
        disciplina_ofertada = localizar_disciplina_ofertada(solicitacao['id_disciplina_ofertada'])
        professor = localizar_professor(disciplina_ofertada.id_professor)
        disciplina = localizar_disciplina(disciplina_ofertada.id_disciplina)
        
        item['nome_aluno'] = aluno.nome
        item['nome_professor'] = professor.nome
        item['nome_disciplina'] = disciplina.nome
        item['turma'] = disciplina_ofertada.turma
        item['ano'] = disciplina_ofertada.ano
        item['semestre'] = disciplina_ofertada.semestre
        
        relatorio.append(item)  
    
        
    return jsonify(relatorio)


if __name__ == '__main__':
    app.run(host='localhost', port=5000)
