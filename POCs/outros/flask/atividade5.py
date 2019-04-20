from flask import Flask, jsonify, request
from DB import database
import Aluno
import Professor
import Coordenador
import Disciplina
import Disciplina_Ofertada
import Solicitacao_Matricula
import json

app = Flask(__name__)

@app.route('/')
def all():
    return jsonify(database)

# ********************************************************************* ALUNOS

@app.route('/alunos')
def alunos():
    result = Aluno.listar()
    json_string = json.dumps([ob.__dict__ for ob in result])
    return json_string

@app.route('/alunos', methods=['POST'])
def novo_aluno():
    novo_aluno.id   = int(request.args.get('id'))
    novo_aluno.nome = str(request.args.get('nome'))
        
    try:
        result = Aluno.incluir(novo_aluno)
        json_string = json.dumps([ob.__dict__ for ob in result])
        return json_string
    except Exception as err:
        print(str(err))
        return str(err), 500

@app.route('/alunos/<int:id_aluno>', methods=['GET'])
def localiza_aluno(id_aluno):
    aluno = Aluno.localizar(id_aluno)
    if aluno == None:
        return jsonify(aluno.__dic__)
    else:
        return '', 404   

@app.route('/alunos/<int:id_aluno>', methods=['DELETE'])
def remover_aluno(id_aluno):
    result = Aluno.deletar(id_aluno)
    if result == None:        
        return 'Não encontrado', 404
    else:
        return 'Excluído'

@app.route('/alunos/<int:id_aluno>', methods=['PUT'])
def atualizar_aluno(id_aluno):    
    aluno = Aluno.localizar(id_aluno)
    novo_aluno.id   = int(request.args.get('id'))
    novo_aluno.nome = str(request.args.get('nome'))
    
    if aluno == None:
        return 'Não encontrado', 404
    else:
        Aluno.alterar(id_aluno, novo_aluno)
        return  'Atualizado'

# **************************************************************** PROFESSORES

@app.route('/professores')
def professores():
    result = Professor.listar()
    json_string = json.dumps([ob.__dict__ for ob in result])
    return json_string

@app.route('/professores', methods=['POST'])
def novo_professor():
    novo_professor.id = int(request.args.get('id'))
    novo_professor.nome = str(request.args.get('nome'))    
        
    try:
        result = Professor.incluir(novo_professor)
        json_string = json.dumps([ob.__dict__ for ob in result])
        return json_string    
    except Exception as err:
        print(str(err))
        return str(err), 500

@app.route('/professores/<int:id_professor>', methods=['GET'])
def localiza_professor(id_professor):
    professor = Professor.localizar(id_professor)
    if professor == None:
        return jsonify(professor.__dic__)
    else:
        return '', 404   

@app.route('/professores/<int:id_professor>', methods=['DELETE'])
def remover_professor(id_professor):
    result = Professor.deletar(id_professor)
    if result == None:        
        return 'Não encontrado', 404
    else:
        return 'Excluído'

@app.route('/professores/<int:id_professor>', methods=['PUT'])
def atualizar_professor(id_professor):    
    professor = Professor.localizar(id_professor)
    novo_professor.id   = int(request.args.get('id'))
    novo_professor.nome = str(request.args.get('nome'))    
        
    if professor == None:
        return 'Não encontrado', 404        
    else:
        Professor.alterar(id_professor, novo_professor)
        return 'Atualizado'

# ************************************************************** COORDENADORES

@app.route('/coordenadores')
def coordenadores():
    result = Coordenador.listar()
    json_string = json.dumps([ob.__dict__ for ob in result])
    return json_string

@app.route('/coordenadores', methods=['POST'])
def novo_coordenador():
    novo_coordenador.id   = int(request.args.get('id'))
    novo_coordenador.nome = str(request.args.get('nome'))    
        
    try:
        result = Coordenador.incluir(novo_coordenador)
        json_string = json.dumps([ob.__dict__ for ob in result])
        return json_string    
    except Exception as err:
        print(str(err))
        return str(err), 500
    
@app.route('/coordenadores/<int:id_coordenador>', methods=['GET'])
def localiza_coordenador(id_coordenador):
    coordenador = Coordenador.localizar(id_coordenador)
    if coordenador == None:
        return jsonify(coordenador.__dic__)
    else:
        return '', 404   

@app.route('/coordenadores/<int:id_coordenador>', methods=['DELETE'])
def remover_coordenador(id_coordenador):
    result = Coordenador.deletar(id_coordenador)
    if result == None:        
        return 'Não encontrado', 404
    else:
        return 'Excluído'

@app.route('/coordenadores/<int:id_coordenador>', methods=['PUT'])
def atualizar_coordenador(id_coordenador):    
    coordenador = Coordenador.localizar(id_coordenador)
    novo_coordenador.id   = int(request.args.get('id'))
    novo_coordenador.nome = str(request.args.get('nome'))    
    
    if coordenador == None:
        return 'Não encontrado', 404
    else:
        Coordenador.alterar(id_coordenador, novo_coordenador)
        return  'Atualizado'    
    
# **************************************************************** DISCIPLINAS

@app.route('/disciplinas')
def disciplinas():
    result = Disciplina.listar()
    json_string = json.dumps([ob.__dict__ for ob in result])
    return json_string


@app.route('/disciplinas', methods=['POST'])
def novo_disciplina():
    novo_disciplina.id             = int(request.args.get('id'))
    novo_disciplina.nome           = str(request.args.get('nome'))
    novo_disciplina.status         = int(request.args.get('status'))
    novo_disciplina.plano_ensino   = str(request.args.get('plano_ensino'))
    novo_disciplina.carga_horaria  = int(request.args.get('carga_horaria'))
    novo_disciplina.id_coordenador = int(request.args.get('id_coordenador'))
        
    try:
        result = Disciplina.incluir(novo_disciplina)
        json_string = json.dumps([ob.__dict__ for ob in result])
        return json_string    
    except Exception as err:
        print(str(err))
        return str(err), 500
    
@app.route('/disciplinas/<int:id_disciplina>', methods=['GET'])
def localiza_disciplina(id_disciplina):
    disciplina = Disciplina.localizar(id_disciplina)
    if disciplina == None:
        return jsonify(disciplina.__dic__)
    else:
        return '', 404   

@app.route('/disciplinas/<int:id_disciplina>', methods=['DELETE'])
def remover_disciplina(id_disciplina):
    result = Disciplina.deletar(id_disciplina)
    if result == None:        
        return 'Não encontrado', 404
    else:
        return 'Excluído'

@app.route('/disciplinas/<int:id_disciplina>', methods=['PUT'])
def atualizar_disciplina(id_disciplina):    
    disciplina = Disciplina.localizar(id_disciplina)
    novo_disciplina.id             = int(request.args.get('id'))
    novo_disciplina.nome           = str(request.args.get('nome'))
    novo_disciplina.status         = int(request.args.get('status'))
    novo_disciplina.plano_ensino   = str(request.args.get('plano_ensino'))
    novo_disciplina.carga_horaria  = int(request.args.get('carga_horaria'))
    novo_disciplina.id_coordenador = int(request.args.get('id_coordenador'))
    
    if disciplina == None:
        return 'Não encontrado', 404
    else:
        Disciplina.alterar(id_disciplina, novo_disciplina)
        return  'Atualizado'        
    
# ****************************************************** DISCIPLINAS_OFERTADAS

@app.route('/disciplinas_ofertadas')
def disciplinas_ofertadas():
    result = Disciplina_Ofertada.listar()
    json_string = json.dumps([ob.__dict__ for ob in result])
    return json_string

@app.route('/disciplinas_ofertadas', methods=['POST'])
def nova_disciplina_ofertada():
    nova_disciplina_ofertada.id             = int(request.args.get('id'))
    nova_disciplina_ofertada.id_disciplina  = int(request.args.get('id_disciplina'))
    nova_disciplina_ofertada.id_professor   = int(request.args.get('id_professor'))
    nova_disciplina_ofertada.ano            = int(request.args.get('ano'))
    nova_disciplina_ofertada.semestre       = int(request.args.get('semestre'))
    nova_disciplina_ofertada.turma          = str(request.args.get('turma'))
    nova_disciplina_ofertada.id_curso       = int(request.args.get('id_curso'))
    nova_disciplina_ofertada.data           = str(request.args.get('data'))
        
    try:
        result = Disciplina_Ofertada.incluir(nova_disciplina_ofertada)
        json_string = json.dumps([ob.__dict__ for ob in result])
        return json_string    
    except Exception as err:
        print(str(err))
        return str(err), 500    

@app.route('/disciplinas_ofertadas/<int:id_disciplina_ofertada>', methods=['GET'])
def localiza_disciplina_ofertada(id_disciplina_ofertada):
    disciplina_ofertada = Disciplina_Ofertada.localizar(id_disciplina_ofertada)
    if disciplina_ofertada == None:
        return jsonify(disciplina_ofertada.__dic__)
    else:
        return '', 404   

@app.route('/disciplinas_ofertadas/<int:id_disciplina_ofertada>', methods=['DELETE'])
def remover_disciplina_ofertada(id_disciplina_ofertada):
    result = Disciplina_Ofertada.deletar(id_disciplina_ofertada)
    if result == None:        
        return 'Não encontrado', 404
    else:
        return 'Excluído'

@app.route('/disciplinas_ofertadas/<int:id_disciplina_ofertada>', methods=['PUT'])
def atualizar_disciplina_ofertada(id_disciplina_ofertada):    
    disciplina_ofertada = Disciplina_Ofertada.localizar(id_disciplina_ofertada)
    nova_disciplina_ofertada.id             = int(request.args.get('id'))
    nova_disciplina_ofertada.id_disciplina  = int(request.args.get('id_disciplina'))
    nova_disciplina_ofertada.id_professor   = int(request.args.get('id_professor'))
    nova_disciplina_ofertada.ano            = int(request.args.get('ano'))
    nova_disciplina_ofertada.semestre       = int(request.args.get('semestre'))
    nova_disciplina_ofertada.turma          = str(request.args.get('turma'))
    nova_disciplina_ofertada.id_curso       = int(request.args.get('id_curso'))
    nova_disciplina_ofertada.data           = str(request.args.get('data'))

    if disciplina_ofertada == None:
        return 'Não encontrado', 404
    else:
        Disciplina_Ofertada.alterar(id_disciplina_ofertada, nova_disciplina_ofertada)
        return  'Atualizado'            

# ***************************************************** SOLICITACAO_MATRICULAS

@app.route('/solicitacao_matriculas')
def solicitacao_matriculas():
    result = Solicitacao_Matricula.listar()
    json_string = json.dumps([ob.__dict__ for ob in result])
    return json_string

@app.route('/solicitacao_matriculas', methods=['POST'])
def nova_solicitacao_matricula():
    nova_solicitacao_matricula.id                     = int(request.args.get('id'))
    nova_solicitacao_matricula.id_aluno               = int(request.args.get('id_aluno'))
    nova_solicitacao_matricula.id_disciplina_ofertada = int(request.args.get('id_disciplina_ofertada'))
    nova_solicitacao_matricula.dt_solicitacao         = str(request.args.get('dt_solicitacao'))
    nova_solicitacao_matricula.id_coordenador         = int(request.args.get('id_coordenador'))
    nova_solicitacao_matricula.status                 = int(request.args.get('status'))
        
    try:
        result = Solicitacao_Matricula.incluir(nova_solicitacao_matricula)
        json_string = json.dumps([ob.__dict__ for ob in result])
        return json_string    
    except Exception as err:
        print(str(err))
        return str(err), 500      

@app.route('/solicitacao_matriculas/<int:id_solicitacao_matricula>', methods=['GET'])
def localiza_solicitacao_matricula(id_solicitacao_matricula):
    solicitacao_matricula = Solicitacao_Matricula.localizar(id_solicitacao_matricula)
    if solicitacao_matricula == None:
        return jsonify(solicitacao_matricula.__dic__)
    else:
        return '', 404   

@app.route('/solicitacao_matriculas/<int:id_solicitacao_matricula>', methods=['DELETE'])
def remover_solicitacao_matricula(id_solicitacao_matricula):
    result = Solicitacao_Matricula.deletar(id_solicitacao_matricula)
    if result == None:        
        return 'Não encontrado', 404
    else:
        return 'Excluído'

@app.route('/solicitacao_matriculas/<int:id_solicitacao_matricula>', methods=['PUT'])
def atualizar_solicitacao_matricula(id_solicitacao_matricula):    
    solicitacao_matricula = Solicitacao_Matricula.localizar(id_solicitacao_matricula)
    nova_solicitacao_matricula.id                     = int(request.args.get('id'))
    nova_solicitacao_matricula.id_aluno               = int(request.args.get('id_aluno'))
    nova_solicitacao_matricula.id_disciplina_ofertada = int(request.args.get('id_disciplina_ofertada'))
    nova_solicitacao_matricula.dt_solicitacao         = str(request.args.get('dt_solicitacao'))
    nova_solicitacao_matricula.id_coordenador         = int(request.args.get('id_coordenador'))
    nova_solicitacao_matricula.status                 = int(request.args.get('status'))
    
    if solicitacao_matricula == None:
        return 'Não encontrado', 404
    else:
        Solicitacao_Matricula.alterar(id_solicitacao_matricula, nova_solicitacao_matricula)
        return  'Atualizado'

# *********************************************************************** MAIN
        
if __name__ == '__main__':
    print('Serviço iniciado na porta 5000...')
    app.run(host='localhost', port=5000)
print('Serviço Finalizado...')
