from Tabela import Tabela

class Professor(Tabela):
    def __init__(self):
        self.id = -1
        self.nome = ''
        
    def validate(self):
        if self.id == -1:
            raise ValidationError('Professor: ID não foi preenchido')
            
        if self.nome == '':
            raise ValidationError('Professor: Nome não foi preenchido')        