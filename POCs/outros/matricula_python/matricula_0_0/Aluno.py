from DB import database, locate, Tabela, ValidationError

class Aluno(Tabela):
    def __init__(self):
        self.id = -1
        self.nome = ''
    
    def validate(self):
        if self.id == -1:
            raise ValidationError('Aluno: ID não foi preenchido')
            
        if (self.nome == '') or (self.nome == 'None'):
            raise ValidationError('Aluno: Nome não foi preenchido')

def listar():
    return database['ALUNOS']

def incluir(novo_aluno):
    aluno      = Aluno()
    aluno.id   = novo_aluno.id
    aluno.nome = novo_aluno.nome
    aluno.validate()
    if locate('aluno', aluno.id)[0]:
        raise ValidationError('Já existe aluno com o ID informado')
    
    database['ALUNOS'].append(aluno)
    return database['ALUNOS']

def localizar(id_aluno):
    for aluno in database['ALUNOS']:
        if aluno.id == id_aluno:
            return aluno
    return None

def deletar(id_aluno):
    for aluno in database['ALUNOS']:
        if aluno.id == id_aluno:
            database['ALUNOS'].remove(aluno)
            return database['ALUNOS']
    return None

def alterar(id_aluno, dados):
    for aluno in database['ALUNOS']:
        if aluno.id == id_aluno:
            aluno.id   = dados.id
            aluno.nome = dados.nome
            return database['ALUNOS']
    return None