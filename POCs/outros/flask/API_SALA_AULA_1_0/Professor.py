from DB import database, locate, Tabela, ValidationError

class Professor(Tabela):
    def __init__(self):
        self.id = -1
        self.nome = ''
        
    def validate(self):
        if self.id == -1:
            raise ValidationError('Professor: ID não foi preenchido')
            
        if (self.nome == '') or (self.nome == 'None'):
            raise ValidationError('Professor: Nome não foi preenchido')        

def listar():
    return database['PROFESSORES']

def incluir(novo_professor):
    professor = Professor()
    professor.id = novo_professor.id
    professor.nome = novo_professor.nome
    professor.validate()
    if locate('professor', professor.id)[0]:
        raise ValidationError('Já existe Professor com o ID informado')

    database['PROFESSORES'].append(novo_professor)
    return database['PROFESSORES']


def localizar(id_professor):
    for professor in database['PROFESSORES']:
        if professor.id == id_professor:
            return professor
    return None

def deletar(id_professor):
    for professor in database['PROFESSORES']:
        if professor.id == id_professor:
            database['PROFESSORES'].remove(professor)
            return database['PROFESSORES']
    return None

def alterar(id_professor, dados):
    for professor in database['PROFESSORES']:
        if professor.id == id_professor:
            professor.id   = dados.id
            professor.nome = dados.nome
            return database['PROFESSORES']
    return None