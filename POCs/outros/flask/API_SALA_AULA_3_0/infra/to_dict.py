#import json

#def to_dict(obj):
    #return json.dumps(obj, strip_privates = True)
    
import inspect

def to_dict(obj):
    pr = {}
    for name in dir(obj):
        value = getattr(obj, name)
        if not name.startswith('_') and not inspect.ismethod(value):
            pr[name] = value
    return pr    

def to_dict_list(lista):
    resultado = []
    for item in lista:
        resultado.append(to_dict(item))
    return resultado