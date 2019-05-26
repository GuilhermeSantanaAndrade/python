from model.solicitacao_matricula import Solicitacao_matricula
from infra.log import Log

solicitacao_matriculas_db = []

class Solicitacao_matriculaJaExiste(Exception):
    pass

def listar():
    return solicitacao_matriculas_db

def localizar(id):
    for x in solicitacao_matriculas_db:
        if x.id == id:
            return x
    return None

def criar(id, id_aluno, id_disciplina_ofertada, dt_solicitacao, id_coordenador, status):
    if localizar(id) != None:
        raise Solicitacao_matriculaJaExiste()
    log = Log(None)
    criado = Solicitacao_matricula(id, id_aluno, id_disciplina_ofertada, dt_solicitacao, id_coordenador, status)
    solicitacao_matriculas_db.append(criado)
    log.finalizar(criado)
    return criado

def remover(id):
    existente = localizar(id)
    if existente == None:
        return None
    log = Log(existente)
    solicitacao_matriculas_db.remove(existente)
    log.finalizar(None)
    return existente

def atualizar(id_antigo, id_novo, id_aluno, id_disciplina_ofertada, dt_solicitacao, id_coordenador, status):
    existente = localizar(id_antigo)
    if existente == None:
        return None
    if id_antigo != id_novo:
        colisao = localizar(id_novo)
        if colisao != None:
            raise Solicitacao_matriculaJaExiste()
    log = Log(existente)
    existente.atualizar(id, id_aluno, id_disciplina_ofertada, dt_solicitacao, id_coordenador, status)
    log.finalizar(existente)
    return existente