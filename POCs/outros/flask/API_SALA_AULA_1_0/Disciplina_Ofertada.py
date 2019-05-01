from DB import database, locate, Tabela, ValidationError
from datetime import date

class Disciplina_Ofertada(Tabela):
    def __init__(self):
        self.id = -1
        self.id_disciplina = -1
        self.id_professor = -1
        self.ano = -1
        self.semestre = -1
        self.turma = ''
        self.id_curso = -1
        self.data = date(1900,1,1)
        
    def validate(self):
        if self.id == -1:
            raise ValidationError('Disciplina_Ofertada: ID não foi preenchido')
            
        if self.id_disciplina == -1:
            raise ValidationError('Disciplina_Ofertada: ID disciplina não foi preenchido')
            
        if self.id_professor == -1:
            raise ValidationError('Disciplina_Ofertada: ID professor ofertada não foi preenchido')
            
        if self.ano == -1:
            raise ValidationError('Disciplina_Ofertada: ano foi preenchido')
            
        if self.semestre == -1:
            raise ValidationError('Disciplina_Ofertada: semestre foi preenchido')
            
        if (self.turma == '') or (self.turma == 'None'):
            raise ValidationError('Disciplina_Ofertada: turma foi preenchido')
            
        if not locate('disciplina', self.id_disciplina)[0]:
            raise ValidationError('Disciplina_Ofertada: Não existe disciplina com o ID informado')
            
        if not locate('professor', self.id_professor)[0]:
            raise ValidationError('Disciplina_Ofertada: Não existe professor com o ID informado')
        
        for item in database['DISCIPLINAS_OFERTADAS']:
            if (self.id_disciplina == item.id_disciplina) and (self.ano == item.ano) and (self.semestre == item.semestre) and (self.turma == item.turma) and (self.id_curso == item.id_curso):
                raise ValidationError('Disciplina_Ofertada: Violação de chave única (id_disciplina, ano, semestre, turma, id_curso)')

def listar():
    return database['DISCIPLINAS_OFERTADAS']

def incluir(nova_disciplina_ofertada):
    disciplina_ofertada                = Disciplina_Ofertada()
    disciplina_ofertada.id             = nova_disciplina_ofertada.id
    disciplina_ofertada.id_disciplina  = nova_disciplina_ofertada.id_disciplina
    disciplina_ofertada.id_professor   = nova_disciplina_ofertada.id_professor
    disciplina_ofertada.ano            = nova_disciplina_ofertada.ano
    disciplina_ofertada.semestre       = nova_disciplina_ofertada.semestre
    disciplina_ofertada.turma          = nova_disciplina_ofertada.turma
    disciplina_ofertada.id_curso       = nova_disciplina_ofertada.id_curso
    disciplina_ofertada.data           = nova_disciplina_ofertada.data
    disciplina_ofertada.validate()
    if locate('disciplina_ofertada', disciplina_ofertada.id)[0]:
        raise ValidationError('Já existe disciplina ofertada com o ID informado')
        
    database['DISCIPLINAS_OFERTADAS'].append(nova_disciplina_ofertada)
    return database['DISCIPLINAS_OFERTADAS']


def localizar(id_disciplina_ofertada):
    for disciplina_ofertada in database['DISCIPLINAS_OFERTADAS']:
        if disciplina_ofertada.id == id_disciplina_ofertada:
            return disciplina_ofertada
    return None

def deletar(id_disciplina_ofertada):
    for disciplina_ofertada in database['DISCIPLINAS_OFERTADAS']:
        if disciplina_ofertada.id == id_disciplina_ofertada:
            database['DISCIPLINAS_OFERTADAS'].remove(disciplina_ofertada)
            return database['DISCIPLINAS_OFERTADAS']
    return None

def alterar(id_disciplina_ofertada, dados):
    for disciplina_ofertada in database['DISCIPLINAS_OFERTADAS']:
        if disciplina_ofertada.id == id_disciplina_ofertada:
            disciplina_ofertada.id             = dados.id
            disciplina_ofertada.id_disciplina  = dados.id_disciplina
            disciplina_ofertada.id_professor   = dados.id_professor
            disciplina_ofertada.ano            = dados.ano
            disciplina_ofertada.semestre       = dados.semestre
            disciplina_ofertada.turma          = dados.turma
            disciplina_ofertada.id_curso       = dados.id_curso
            disciplina_ofertada.data           = dados.data
            
            return database['DISCIPLINAS_OFERTADAS']
    return None