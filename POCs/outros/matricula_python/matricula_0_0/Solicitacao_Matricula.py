from DB import database, locate, Tabela, ValidationError
from datetime import date

class Solicitacao_Matricula(Tabela):
    def __init__(self):
        self.id = -1
        self.id_aluno = -1
        self.id_disciplina_ofertada = -1
        self.dt_solicitacao = date(1900,1,1)
        self.id_coordenador = -1
        self.status = -1
        
    def validate(self):
        if self.id == -1:
            raise ValidationError('SolicitacaoMatricula: ID não foi preenchido')
            
        if self.id_aluno == -1:
            raise ValidationError('SolicitacaoMatricula: ID Aluno não foi preenchido')
            
        if self.id_disciplina_ofertada == -1:
            raise ValidationError('SolicitacaoMatricula: ID disciplina ofertada não foi preenchido')            
            
        if not(self.status in [1,2,3,4,5,6]):
            raise ValidationError('SolicitacaoMatricula: Valor inválido para campo Status')       
            
        if not locate('aluno', self.id_aluno)[0]:
            raise ValidationError('Não existe aluno com o ID informado')
            
        if not locate('disciplina_Ofertada', self.id_disciplina_ofertada)[0]:
            raise ValidationError('Não existe disciplina ofertada com o ID informado')

        if not locate('coordenador', self.id_coordenador)[0]:
            raise ValidationError('Não existe coordenador com o ID informado')            
            
def listar():
    return database['SOLICITACAO_MATRICULAS']

def incluir(nova_solicitacao_matricula):
    solicitacao_matricula                        = Solicitacao_Matricula()
    solicitacao_matricula.id                     = nova_solicitacao_matricula.id
    solicitacao_matricula.id_aluno               = nova_solicitacao_matricula.id_aluno
    solicitacao_matricula.id_disciplina_ofertada = nova_solicitacao_matricula.id_disciplina_ofertada
    solicitacao_matricula.dt_solicitacao         = nova_solicitacao_matricula.dt_solicitacao
    solicitacao_matricula.id_coordenador         = nova_solicitacao_matricula.id_coordenador
    solicitacao_matricula.status                 = nova_solicitacao_matricula.status
    solicitacao_matricula.validate()
    if locate('solicitacao_matricula', solicitacao_matricula.id)[0]:
        raise ValidationError('Já existe solicitação matricula com o ID informado')
        
    database['SOLICITACAO_MATRICULAS'].append(nova_solicitacao_matricula)
    return database['SOLICITACAO_MATRICULAS']


def localizar(id_solicitacao_matricula):
    for solicitacao_matricula in database['SOLICITACAO_MATRICULAS']:
        if solicitacao_matricula.id == id_solicitacao_matricula:
            return solicitacao_matricula
    return None

def deletar(id_solicitacao_matricula):
    for solicitacao_matricula in database['SOLICITACAO_MATRICULAS']:
        if solicitacao_matricula.id == id_solicitacao_matricula:
            database['SOLICITACAO_MATRICULAS'].remove(solicitacao_matricula)
            return database['SOLICITACAO_MATRICULAS']
    return None

def alterar(id_solicitacao_matricula, dados):
    for solicitacao_matricula in database['SOLICITACAO_MATRICULAS']:
        if solicitacao_matricula.id == id_solicitacao_matricula:
            solicitacao_matricula.id                     = dados.id
            solicitacao_matricula.id_aluno               = dados.id_aluno
            solicitacao_matricula.id_disciplina_ofertada = dados.id_disciplina_ofertada
            solicitacao_matricula.dt_solicitacao         = dados.dt_solicitacao
            solicitacao_matricula.id_coordenador         = dados.id_coordenador
            solicitacao_matricula.status                 = dados.status
            
            return database['SOLICITACAO_MATRICULAS']
    return None