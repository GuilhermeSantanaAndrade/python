from DB import database, locate, Tabela, ValidationError

class Disciplina(Tabela):
    def __init__(self):
        self.id = -1
        self.nome = ''
        self.status = -1
        self.plano_ensino = ''
        self.carga_horaria = -1
        self.id_coordenador = -1
        
    def validate(self):
        if self.id == -1:
            raise ValidationError('Disciplina: ID não foi preenchido')
            
        if (self.nome == '') or (self.nome == 'None'):
            raise ValidationError('Disciplina: Nome não foi preenchido')
                        
        if (not ((self.status == 0) or (self.status == 1)))  :
            raise ValidationError('Disciplina: Valor do campo Status está inválido')
            
        if self.carga_horaria == -1:
            raise ValidationError('Disciplina: Carga horária está inválido')
        
        if not locate('coordenador', self.id_coordenador)[0]:
            raise ValidationError('Não existe coordenador com o ID informado') 
            
def listar():
    return database['DISCIPLINAS']

def incluir(nova_disciplina):
    disciplina                = Disciplina()
    disciplina.id             = nova_disciplina.id
    disciplina.nome           = nova_disciplina.nome
    disciplina.status         = nova_disciplina.status
    disciplina.plano_ensino   = nova_disciplina.plano_ensino
    disciplina.carga_horaria  = nova_disciplina.carga_horaria
    disciplina.id_coordenador = nova_disciplina.id_coordenador
    disciplina.validate()
    if locate('disciplina', disciplina.id)[0]:
        raise ValidationError('Já existe disciplina com o ID informado')
        
    database['DISCIPLINAS'].append(nova_disciplina)
    return database['DISCIPLINAS']


def localizar(id_disciplina):
    for disciplina in database['DISCIPLINAS']:
        if disciplina.id == id_disciplina:
            return disciplina
    return None

def deletar(id_disciplina):
    for disciplina in database['DISCIPLINAS']:
        if disciplina.id == id_disciplina:
            database['DISCIPLINAS'].remove(disciplina)
            return database['DISCIPLINAS']
    return None

def alterar(id_disciplina, dados):
    for disciplina in database['DISCIPLINAS']:
        if disciplina.id == id_disciplina:
            disciplina.id             = dados.id
            disciplina.nome           = dados.nome
            disciplina.status         = dados.status
            disciplina.plano_ensino   = dados.plano_ensino
            disciplina.carga_horaria  = dados.carga_horaria
            disciplina.id_coordenador = dados.id_coordenador
            
            return database['DISCIPLINAS']
    return None