from model.professor import Professor
from infra.log import Log

professores_db = []

class ProfessorJaExiste(Exception):
    pass

def listar():
    return professores_db

def localizar(id):
    for x in professores_db:
        if x.id == id:
            return x
    return None

def criar(id, nome):
    if localizar(id) != None:
        raise ProfessorJaExiste()
    log = Log(None)
    criado = Professor(id, nome)
    professores_db.append(criado)
    log.finalizar(criado)
    return criado

def remover(id):
    existente = localizar(id)
    if existente == None:
        return None
    log = Log(existente)
    professores_db.remove(existente)
    log.finalizar(None)
    return existente

def atualizar(id_antigo, id_novo, nome):
    existente = localizar(id_antigo)
    if existente == None:
        return None
    if id_antigo != id_novo:
        colisao = localizar(id_novo)
        if colisao != None:
            raise ProfessorJaExiste()
    log = Log(existente)
    existente.atualizar(id_novo, nome)
    log.finalizar(existente)
    return existente