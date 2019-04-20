from Tabela import Tabela, ValidationError
from datetime import date

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
            
        if self.nome == '':
            raise ValidationError('Disciplina: Nome não foi preenchido')
                        
        if not ((self.status == '0') or (self.status == '1')) :
            raise ValidationError('Disciplina: Valor do campo Status está inválido')
            
        if self.carga_horaria == -1:
            raise ValidationError('Disciplina: Carga horária está inválido')
            
        
class DisciplinaOfertada(Tabela):
    def __init__(self):
        self.id = -1
        self.id_disciplina = -1
        self.id_professor = -1
        self.ano = -1
        self.semestre = -1
        self.turma = ''
        self.data = date(1900,1,1)
        
    def validate(self):
        if self.id == -1:
            raise ValidationError('SolicitacaoMatricula: ID não foi preenchido')
            
        if self.id_disciplina == -1:
            raise ValidationError('SolicitacaoMatricula: ID disciplina não foi preenchido')
            
        if self.id_professor == -1:
            raise ValidationError('SolicitacaoMatricula: ID professor ofertada não foi preenchido')
            
        if self.ano == -1:
            raise ValidationError('SolicitacaoMatricula: ano foi preenchido')
            
        if self.semestre == -1:
            raise ValidationError('SolicitacaoMatricula: semestre foi preenchido')            
            
        if self.turma == -1:
            raise ValidationError('SolicitacaoMatricula: turma foi preenchido')            