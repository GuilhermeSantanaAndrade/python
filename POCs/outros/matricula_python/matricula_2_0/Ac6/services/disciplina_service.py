from model.disciplina import Disciplina
from infra.log import Log

disciplinas_db = []

class DisciplinaJaExiste(Exception):
    pass

def listar():
    return disciplinas_db

def localizar(id):
    for x in disciplinas_db:
        if x.id == id:
            return x
    return None

def criar(id, nome, status, plano_ensino, carga_horaria, id_coordenador):
    if localizar(id) != None:
        raise DisciplinaJaExiste()
    log = Log(None)
    criado = Disciplina(id, nome, status, plano_ensino, carga_horaria, id_coordenador)
    disciplinas_db.append(criado)
    log.finalizar(criado)
    return criado

def remover(id):
    existente = localizar(id)
    if existente == None:
        return None
    log = Log(existente)
    disciplinas_db.remove(existente)
    log.finalizar(None)
    return existente

def atualizar(id_antigo, id_novo, nome, status, plano_ensino, carga_horaria, id_coordenador):
    existente = localizar(id_antigo)
    if existente == None:
        return None
    if id_antigo != id_novo:
        colisao = localizar(id_novo)
        if colisao != None:
            raise DisciplinaJaExiste()
    log = Log(existente)
    existente.atualizar(id_novo, nome, status, plano_ensino, carga_horaria, id_coordenador)
    log.finalizar(existente)
    return existente