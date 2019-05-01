from model.aluno import Aluno
from infra.log import Log

alunos_db = []

class AlunoJaExiste(Exception):
    pass

def listar():
    return alunos_db

def localizar(id):
    for x in alunos_db:
        if x.id == id:
            return x
    return None

def criar(id, nome):
    if localizar(id) != None:
        raise AlunoJaExiste()
    log = Log(None)
    criado = Aluno(id, nome)
    alunos_db.append(criado)
    log.finalizar(criado)
    return criado

def remover(id):
    existente = localizar(id)
    if existente == None:
        return None
    log = Log(existente)
    alunos_db.remove(existente)
    log.finalizar(None)
    return existente

def atualizar(id_antigo, id_novo, nome):
    existente = localizar(id_antigo)
    if existente == None:
        return None
    if id_antigo != id_novo:
        colisao = localizar(id_novo)
        if colisao != None:
            raise AlunoJaExiste()
    log = Log(existente)
    existente.atualizar(id_novo, nome)
    log.finalizar(existente)
    return existente