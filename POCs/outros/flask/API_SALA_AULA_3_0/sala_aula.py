from flask import Flask, jsonify
from alunos_api import alunos_app
from professores_api import professores_app
from coordenadores_api import coordenadores_app
from cursos_api import cursos_app
from disciplina_api import disciplinas_app
from disciplina_ofertada_api import disciplina_ofertadas_app
from solicitacao_matricula_api import solicitacao_matriculas_app
from infra.to_dict import to_dict_list

app = Flask(__name__)
app.register_blueprint(alunos_app)
app.register_blueprint(professores_app)
app.register_blueprint(coordenadores_app)
app.register_blueprint(cursos_app)
app.register_blueprint(disciplinas_app)
app.register_blueprint(disciplina_ofertadas_app)
app.register_blueprint(solicitacao_matriculas_app)

@app.route('/')
def all():
    from services.professor_service import listar as listar_professores    
    from services.aluno_service import listar as listar_alunos
    from services.coordenador_service import listar as listar_coordenadores
    from services.curso_service import listar as listar_cursos
    from services.disciplina_service import listar as listar_disciplinas
    from services.disciplina_ofertada_service import listar as listar_disciplina_ofertadas
    from services.solicitacao_matricula_service import listar as listar_solicitacao_matriculas
    
    database = { 
        "ALUNOS": to_dict_list(listar_alunos()),
        "PROFESSORES": to_dict_list(listar_professores()),
        "COORDENADORES": to_dict_list(listar_coordenadores()),
        "CURSOS": to_dict_list(listar_cursos()),
        "DISCIPLINAS": to_dict_list(listar_disciplinas()),
        "DISCIPLINA_OFERTADAS": to_dict_list(listar_disciplina_ofertadas()),
        "SOLICITACAO_MATRICULA": to_dict_list(listar_solicitacao_matriculas())
    }
    return jsonify(database)

@app.route('/relatorio')
def report():
    from services.professor_service import localizar as localizar_professor
    from services.aluno_service import localizar as localizar_aluno
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
