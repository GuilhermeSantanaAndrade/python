from Tabela import Tabela, ValidationError

class Aluno(Tabela):
    def __init__(self):
        self.id = -1
        self.nome = ''
    
    def __str__(self):
        return 'id: %i / nome: %s' %(self.id, self.nome)
    
    def validate(self):
        if self.id == -1:
            raise ValidationError('Aluno: ID não foi preenchido')
            
        if self.nome == '':
            raise ValidationError('Aluno: Nome não foi preenchido')