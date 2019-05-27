from model.mensagem import Mensagem
from infra.log import Log

from dao.mensagem_dao import \
    listar as listar_dao, \
    criar as criar_dao, \
    localizar as localizar_dao,\
    remover as remover_dao,\
    atualizar as atualizar_dao

class MensagemJaExiste(Exception):
    pass

def listar():
    return listar_dao()

def localizar(id):
    return localizar_dao(id)

def criar(id, id_remetente, id_destinatario, texto):
    if localizar(id) != None:
        raise MensagemJaExiste()
    log = Log(None)
    criado = Mensagem(id, id_remetente, id_destinatario, texto)
    criar_dao(criado)
    log.finalizar(criado)
    return criado

def remover(id):
    existente = localizar(id)
    if existente == None:
        return None
    log = Log(existente)
    remover_dao(id)
    log.finalizar(None)
    return existente

def atualizar(id_antigo, id_novo, id_remetente, id_destinatario, texto):
    existente = localizar(id_antigo)
    if existente == None:
        return None
    if id_antigo != id_novo:
        colisao = localizar(id_novo)
        if colisao != None:
            raise MensagemJaExiste()
    log = Log(existente)
    atualizar_dao(id_antigo, id_novo, id_remetente, id_destinatario, texto)
    novo = Mensagem(id_novo, id_remetente, id_destinatario, texto)
    log.finalizar(novo)
    return novo
