from model.coordenador import Coordenador
from infra.log import Log

coordenadores_db = []

class CoordenadorJaExiste(Exception):
    pass

def listar():
    return coordenadores_db

def localizar(id):
    for x in coordenadores_db:
        if x.id == id:
            return x
    return None

def criar(id, nome):
    if localizar(id) != None:
        raise CoordenadorJaExiste()
    log = Log(None)
    criado = Coordenador(id, nome)
    coordenadores_db.append(criado)
    log.finalizar(criado)
    return criado

def remover(id):
    existente = localizar(id)
    if existente == None:
        return None
    log = Log(existente)
    coordenadores_db.remove(existente)
    log.finalizar(None)
    return existente

def atualizar(id_antigo, id_novo, nome):
    existente = localizar(id_antigo)
    if existente == None:
        return None
    if id_antigo != id_novo:
        colisao = localizar(id_novo)
        if colisao != None:
            raise CoordenadorJaExiste()
    log = Log(existente)
    existente.atualizar(id_novo, nome)
    log.finalizar(existente)
    return existente