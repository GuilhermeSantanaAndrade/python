from flask import Flask, jsonify
from alunos_api import alunos_app
from professores_api import professores_app
from coordenadores_api import coordenadores_app
from cursos_api import cursos_app
from disciplina_api import disciplinas_app
from disciplina_ofertada_api import disciplina_ofertadas_app
from solicitacao_matricula_api import solicitacao_matriculas_app

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
    from services.professores_service import listar as listar_professores    
    from services.alunos_service import listar as listar_alunos
    from services.coordenador_service import listar as listar_coordenadores
    from services.cursos_service import listar as listar_cursos
    from services.disciplinas_service import listar as listar_disciplinas
    from services.disciplina_ofertadas_service import listar as listar_disciplina_ofertadas
    from services.solicitacao_matriculas_service import listar as listar_solicitacao_matriculas
    
    database = {
        "ALUNOS": listar_alunos(),
        "PROFESSORES": listar_professores(),
        "COORDENADORES": listar_coordenadores(),
        "CURSOS": listar_cursos(),
        "DISCIPLINAS": listar_disciplinas(),
        "DISCIPLINA_OFERTADAS": listar_disciplina_ofertadas(),
        "SOLICITACAO_MATRICULA": listar_solicitacao_matriculas()
    }
    return jsonify(database)

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
