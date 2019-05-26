from flask import Flask, jsonify,request

app = Flask(__name__)

database = dict()
database['ALUNO'] = []
database['PROFESSOR'] = []


@app.route('/')
def all():
    return jsonify(database)
@app.route('/alunos')
def alunos():
    return jsonify(database['ALUNO'])
@app.route('/professores')
def professores():
    return jsonify(database['PROFESSOR'])

@app.route('/alunos', methods=['POST'])
def novo_aluno():
    novo_aluno = request.get_json()
    database['ALUNO'].append(novo_aluno)
    return jsonify(database['ALUNO'])


@app.route('/alunos/<int:id_aluno>', methods=['GET'])
def localiza_aluno(id_aluno):
    for aluno in database['ALUNO']:
        if aluno['id'] == id_aluno:
            return jsonify(aluno)
    return '', 404    

@app.route('/professores', methods=['POST'])
def novo_professor():
    novo_professor = request.get_json()
    database['PROFESSOR'].append(novo_professor)
    return jsonify(database['PROFESSOR'])


@app.route('/professores/<int:id_professor>', methods=['GET'])
def localiza_professores(id_professor):
    for professores in database['PROFESSOR']:
        if professores['id'] == id_professor:
            return jsonify(professores)
    return '', 404    


@app.route('/alunos/<int:id_aluno>', methods=['DELETE'])
def remover_aluno(id_aluno):
    for aluno in database['ALUNO']:
        if aluno['id'] == id_aluno:
            database['ALUNO'].remove(aluno)
            return jsonify(database['ALUNO'])
    return '', 404    


@app.route('/professores/<int:id_professor>', methods=['DELETE'])
def remover_professor(id_professor):
    for professores in database['PROFESSOR']:
        if professores['id'] == id_professor:
            database['PROFESSOR'].remove(professores)
            return jsonify(database['PROFESSOR'])
    return '', 404


@app.route('/professores/<int:id_professor>', methods=['PUT'])
def atualizar_professor(id_professor):
    for professor in database['PROFESSOR']:
        if professor['id'] == id_professor:
            dados = request.get_json()
            professor['id'] = dados['id']
            professor['nome'] = dados['nome']
            return jsonify(database['PROFESSOR'])
    return '', 404

@app.route('/alunos/<int:id_aluno>', methods=['PUT'])
def atualizar_aluno(id_aluno):
    for aluno in database['ALUNO']:
        if aluno['id'] == id_aluno:
            dados = request.get_json()
            aluno['id'] = dados['id']
            aluno['nome'] = dados['nome']
            return jsonify(database['ALUNO'])
    return '', 404    



if __name__ == '__main__':
    app.run(host='localhost', port=5000)