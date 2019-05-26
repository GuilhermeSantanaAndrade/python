from DB import database, locate, Tabela, ValidationError

class Coordenador(Tabela):
    def __init__(self):
        self.id = -1
        self.nome = ''

    def validate(self):
        if self.id == -1:
            raise ValidationError('Coordenador: ID não foi preenchido')
            
        if (self.nome == '') or (self.nome == 'None'):
            raise ValidationError('Coordenador: Nome não foi preenchido')

def listar():
    return database['COORDENADORES']

def incluir(novo_coordenador):
    coordenador      = Coordenador()
    coordenador.id   = novo_coordenador.id
    coordenador.nome = novo_coordenador.nome
    coordenador.validate()
    if locate('coordenador', coordenador.id)[0]:
        raise ValidationError('Já existe coordenador com o ID informado')
    
    database['COORDENADORES'].append(novo_coordenador)
    return database['COORDENADORES']


def localizar(id_coordenador):
    for coordenador in database['COORDENADORES']:
        if coordenador.id == id_coordenador:
            return coordenador
    return None

def deletar(id_coordenador):
    for coordenador in database['COORDENADORES']:
        if coordenador.id == id_coordenador:
            database['COORDENADORES'].remove(coordenador)
            return database['COORDENADORES']
    return None

def alterar(id_coordenador, dados):
    for coordenador in database['COORDENADORES']:
        if coordenador.id == id_coordenador:
            coordenador.id   = dados.id
            coordenador.nome = dados.nome
            return database['COORDENADORES']
    return None