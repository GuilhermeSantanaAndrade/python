from flask import Flask, jsonify, request
from alunos_api import alunos_app, alunos_db
from professores_api import professores_app, professores_db
from coordenador_api import coordenador_app,coordenador_db
from disciplina_api import disciplina_app,disciplina_db
from curso_api import curso_app,curso_db
from disciplina_ofertada_api import disciplina_ofertada_app, disciplina_ofertada_db
from solicitacao_matricula_api import solicitacao_matricula_app,solicitacao_matricula_db

database = {
    "ALUNOS": alunos_db,
    "PROFESSORES": professores_db,
    "COORDENADOR": coordenador_db,
    "DISCIPLINA": disciplina_db,
    "CURSO": curso_db,
    "DISCIPLINA_OFERTADA": disciplina_ofertada_db,
    "SOLICITACAO_MATRICULA": solicitacao_matricula_db
}

app = Flask(__name__)
app.register_blueprint(alunos_app)
app.register_blueprint(professores_app)
app.register_blueprint(coordenador_app)
app.register_blueprint(disciplina_app)
app.register_blueprint(curso_app)
app.register_blueprint(disciplina_ofertada_app)
app.register_blueprint(solicitacao_matricula_app)

@app.route('/')
def all():
    return jsonify(database)

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
