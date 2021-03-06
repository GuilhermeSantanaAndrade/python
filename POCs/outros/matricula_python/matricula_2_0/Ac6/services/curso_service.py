from model.curso import Curso
from infra.log import Log

cursos_db = []

class CursoJaExiste(Exception):
    pass

def listar():
    return cursos_db

def localizar(id):
    for x in cursos_db:
        if x.id == id:
            return x
    return None

def criar(id, nome):
    if localizar(id) != None:
        raise CursoJaExiste()
    log = Log(None)
    criado = Curso(id, nome)
    cursos_db.append(criado)
    log.finalizar(criado)
    return criado

def remover(id):
    existente = localizar(id)
    if existente == None:
        return None
    log = Log(existente)
    cursos_db.remove(existente)
    log.finalizar(None)
    return existente

def atualizar(id_antigo, id_novo, nome):
    existente = localizar(id_antigo)
    if existente == None:
        return None
    if id_antigo != id_novo:
        colisao = localizar(id_novo)
        if colisao != None:
            raise CursoJaExiste()
    log = Log(existente)
    existente.atualizar(id_novo, nome)
    log.finalizar(existente)
    return existente