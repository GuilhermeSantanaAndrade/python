from Tabela import Tabela, ValidationError
from datetime import date

class SolicitacaoMatricula(Tabela):
    def __init__(self):
        self.id = -1
        self.id_aluno = -1
        self.id_disciplina_ofertada = -1
        self.dt_solicitacao = date(1900,1,1)
        self.id_coordenador = -1
        self.status = -1
        
    def validate(self):            
        print('aqui')        
        if self.id == -1:
            raise ValidationError('SolicitacaoMatricula: ID não foi preenchido')
            
        if self.id_aluno == -1:
            raise ValidationError('SolicitacaoMatricula: ID Aluno não foi preenchido')
            
        if self.id_disciplina_ofertada == -1:
            raise ValidationError('SolicitacaoMatricula: ID disciplina ofertada não foi preenchido')            
            
        if not(self.status in ['1','2','3','4','5','6']):
            raise ValidationError('SolicitacaoMatricula: Valor inválido para campo Status')            