from flask import Flask, request, jsonify
from infra.db import criar_db, remover_db
from usuario_api import usuarios_app
from mensagem_api import mensagens_app
from geral_api import geral_app

app = Flask(__name__)
app.register_blueprint(usuarios_app)
app.register_blueprint(mensagens_app)
app.register_blueprint(geral_app)

@app.route('/')
def all():
    pass

criar_db() 
#remover_db()

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
