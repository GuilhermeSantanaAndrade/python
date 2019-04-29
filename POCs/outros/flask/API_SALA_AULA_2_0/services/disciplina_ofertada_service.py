from model.disciplina_ofertada import Disciplina_ofertada
from infra.log import Log

disciplina_ofertadas_db = []

class Disciplina_ofertadaJaExiste(Exception):
    pass

def comparar_chave_unica(left, right):
    return left['id_disciplina'] == right['id_disciplina'] and \
            left['ano'] == right['ano'] and \
            left['semestre'] == right['semestre'] and \
            left['turma'] == right['turma'] and \
            left['id_curso'] == right['id_curso']

def listar():
    return disciplina_ofertadas_db

def localizar(id):
    for x in disciplina_ofertadas_db:
        if x.id == id:
            return x
    return None

def criar(id, nome):
    idx = localizar(id)
    if idx != None:
        raise Disciplina_ofertadaJaExiste()
        
    for disc in disciplina_ofertadas_db:
        if comparar_chave_unica(disc, disciplina_ofertadas_db[idx]):
            raise Disciplina_ofertadaJaExiste
        
    log = Log(None)
    criado = Disciplina_ofertada(id, nome)
    disciplina_ofertadas_db.append(criado)
    log.finalizar(criado)
    return criado

def remover(id):
    existente = localizar(id)
    if existente == None:
        return None
    log = Log(existente)
    disciplina_ofertadas_db.remove(existente)
    log.finalizar(None)
    return existente

def atualizar(id_antigo, id_novo, nome):
    existente = localizar(id_antigo)
    if existente == None:
        return None
    if id_antigo != id_novo:
        colisao = localizar(id_novo)
        if colisao != None:
            raise Disciplina_ofertadaJaExiste()
    log = Log(existente)
    existente.atualizar(id_novo, nome)
    log.finalizar(existente)
    return existente