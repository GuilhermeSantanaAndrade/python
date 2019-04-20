from Tabela import Tabela

class Coordenador(Tabela):
    def __init__(self):
        self.id = -1
        self.nome = ''

    def validate(self):
        if self.id == -1:
            raise ValidationError('Coordenador: ID não foi preenchido')
            
        if self.nome == '':
            raise ValidationError('Coordenador: Nome não foi preenchido')