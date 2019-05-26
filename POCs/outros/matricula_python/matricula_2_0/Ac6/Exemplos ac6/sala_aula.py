from flask import Flask, jsonify, request
from alunos_api import alunos_app
from professores_api import professores_app

app = Flask(__name__)
app.register_blueprint(alunos_app)
app.register_blueprint(professores_app)

@app.route('/')
def all():
    from services.professores_service import listar as listar_professores
    #from services.alunos_service import listar as listar_alunos
    database = {
        #"ALUNOS": listar_alunos(),
        "PROFESSORES": listar_professores()
    }
    return jsonify(database)

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
