class ValidationError(Exception):
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
    