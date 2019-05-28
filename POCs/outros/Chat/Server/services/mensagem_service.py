from model.mensagem import Mensagem
from infra.log import Log
from datetime import datetime
from random import random
from services.usuario_service import listar as listar_usuarios, UsuarioNaoExiste, SegredoInvalido
from dao.mensagem_dao import \
    listar as listar_dao, \
    criar as criar_dao, \
    localizar as localizar_dao,\
    localizarRange as localizarRange_dao,\
    remover as remover_dao,\
    atualizar as atualizar_dao

class MensagemJaExiste(Exception):
    pass

def listar():
    return listar_dao()

def localizar(id_msg):
    return localizar_dao(id_msg)

def localizarRange(id_remetente, segredo, inicio, fim):
    usuarios = listar_usuarios()
    found = False
    for usr in usuarios:
        if (usr.id == id_remetente):
            if (usr.segredo != segredo):
                raise SegredoInvalido()
            found = True
            break
    if (not found):
      raise UsuarioNaoExiste('remetente inexistente')

    mensagens = localizarRange_dao(id_remetente, inicio, fim)
    result = []
    for msg in mensagens:
        result.append({"de": msg.id_remetente, "para": msg.id_destinatario, "data_hora": msg.data_hora, "texto": msg.texto})
    return {"mensagens": result}

def criar(segredo, id_remetente, id_destinatario, texto):
    id = getMaxId() + 1
    if localizar(id) != None:
        raise MensagemJaExiste()

    usuarios = listar_usuarios()
    found = False
    for usr in usuarios:
        if (usr.id == id_remetente):
            if (usr.segredo != segredo):
                raise SegredoInvalido()
            found = True
            break
    if (not found):
      raise UsuarioNaoExiste('remetente inexistente')

    found = False
    for usr in usuarios:
        if (usr.id == id_destinatario):
            found = True
            break
    if (not found):
      raise UsuarioNaoExiste('destinatario inexistente')

    data_hora = datetime.now()
    log = Log(None)
    criado = Mensagem(id, id_remetente, id_destinatario, data_hora, texto)
    criar_dao(criado)
    log.finalizar(criado)
    return {"id": criado.id, "data_hora": criado.data_hora}

def remover(id):
    existente = localizar(id)
    if existente == None:
        return None
    log = Log(existente)
    remover_dao(id)
    log.finalizar(None)
    return existente

def atualizar(id_antigo, id_novo, id_remetente, id_destinatario, data_hora, texto):
    existente = localizar(id_antigo)
    if existente == None:
        return None
    if id_antigo != id_novo:
        colisao = localizar(id_novo)
        if colisao != None:
            raise MensagemJaExiste()
    log = Log(existente)
    atualizar_dao(id_antigo, id_novo, id_remetente, id_destinatario, data_hora, texto)
    novo = Mensagem(id_novo, id_remetente, id_destinatario, data_hora, texto)
    log.finalizar(novo)
    return novo

def getMaxId():
    lista = listar()
    maxID = -1
    for msg in lista:
        if (msg.id > maxID):
            maxID = msg.id
    return maxID
