database = dict()
database['ALUNOS'] = []
database['PROFESSORES'] = []
database['COORDENADORES'] = []
database['DISCIPLINAS'] = []
database['DISCIPLINAS_OFERTADAS'] = []
database['SOLICITACAO_MATRICULAS'] = []

class ValidationError(Exception):
    pass

class TableDoesntExists(Exception):
    pass

class Tabela(object):
    def __init__(self):
        pass
    
    def validate():
        pass
    
def find(array, valor):
    idx = -1
    for item in array:
        idx += 1
        if item.id == valor:
            return item, idx
    return None, idx

def locate(tabela, id):
    if tabela.lower() == 'aluno':
        out, idx = find(database['ALUNOS'], id)
        return (out != None), idx, out
    elif tabela.lower() ==  'professor':
        out, idx = find(database['PROFESSORES'], id)
        return (out != None), idx, out
    elif tabela.lower() == 'coordenador':
        out, idx = find(database['COORDENADORES'], id)
        return (out != None), idx, out
    elif tabela.lower() == 'disciplina':
        out, idx = find(database['DISCIPLINAS'], id)
        return (out != None), idx, out
    elif tabela.lower() == 'disciplina_ofertada':
        out, idx = find(database['DISCIPLINAS_OFERTADAS'], id)
        return (out != None), idx, out
    elif tabela.lower() == 'solicitacao_matricula':
        out, idx = find(database['SOLICITACAO_MATRICULAS'], id)
        return (out != None), idx, out
    else:
        raise TableDoesntExists('Classe %s inexistente no Banco de Dados' %(tabela)) 