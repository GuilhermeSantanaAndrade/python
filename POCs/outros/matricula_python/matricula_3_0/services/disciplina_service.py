from model.disciplina import Disciplina
from infra.log import Log

disciplina_db = []

class DisciplinaJaExiste(Exception):
    pass

class CoordenadorNaoExiste(Exception):
    pass

class StatusInvalido(Exception):
    pass

def listar():
    return disciplina_db

def localizar(id):
    for x in disciplina_db:
        if x.id == id:
            return x
    return None

def validaStatus(status):
    if status == 1 or status == 0:
        return True
    else:
        return False

def criar(id, nome, status, plano_ensino, carga_horaria, id_coordenador):
    from services.coordenador_service import localizar as localizar_coordenador
    if not validaStatus(status):
        raise StatusInvalido()
    if localizar(id) != None:
        raise DisciplinaJaExiste()
    if localizar_coordenador(id_coordenador) == None:
        raise CoordenadorNaoExiste()
    log = Log(None)
    criado = Disciplina(id, nome, status, plano_ensino, carga_horaria, id_coordenador)
    disciplina_db.append(criado)
    log.finalizar(criado)
    return criado

def remover(id):
    existente = localizar(id)
    if existente == None:
        return None
    log = Log(existente)
    disciplina_db.remove(existente)
    log.finalizar(None)
    return existente

def atualizar(id_antigo, id_novo, nome, status, plano_ensino, carga_horaria, id_coordenador):
    from services.coordenador_service import localizar as localizar_coordenador
    if not validaStatus(status):
        raise StatusInvalido()
    existente = localizar(id_antigo)
    if existente == None:
        return None
    if id_antigo != id_novo:
        colisao = localizar(id_novo)
        if colisao != None:
            raise DisciplinaJaExiste()

    if localizar_coordenador(id_coordenador) == None:
        raise CoordenadorNaoExiste()

    log = Log(existente)
    existente.atualizar(id_novo, nome, status, plano_ensino, carga_horaria, id_coordenador)
    log.finalizar(existente)
    return existente