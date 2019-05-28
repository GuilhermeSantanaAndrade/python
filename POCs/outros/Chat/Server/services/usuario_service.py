from model.usuario import Usuario
from infra.log import Log
import random
from dao.usuario_dao import \
    listar as listar_dao, \
    criar as criar_dao, \
    localizar as localizar_dao,\
    remover as remover_dao,\
    atualizar as atualizar_dao

class UsuarioJaExiste(Exception):
    pass

class UsuarioNaoExiste(Exception):
    pass

class SegredoInvalido(Exception):
    pass

class UsuarioComDependencia(Exception):
    pass

def listar():
    return listar_dao()

def listarParaFora():
    usuarios = listar_dao()
    result = []
    for usr in usuarios:
        result.append({"id": usr.id, "nome": usr.nome})
    return {"usr": result}


def localizar(id):
    return localizar_dao(id)

def criar(nome):
    usuarios = listar()
    for usr in usuarios:
        if (usr.nome == nome):
            raise UsuarioJaExiste()

    id = random.randint(1, 200)
    segredo = str(random.randint(1, 99999))
        
    log = Log(None)
    criado = Usuario(id, nome, segredo)
    criar_dao(criado)
    log.finalizar(criado)
    return criado

def remover(id):
    from services.mensagem_service import listar as listar_mensagens
    existente = localizar(id)
    if existente == None:
        return None
    listaMensagens = listar_mensagens()
    for msg in listaMensagens:
        if ((msg.id_remetente == id) or (msg.id_destinatario == id)):
            raise UsuarioComDependencia()
    log = Log(existente)
    remover_dao(id)
    log.finalizar(None)
    return existente

def atualizar(id_antigo, id_novo, nome, segredo):
    existente = localizar(id_antigo)
    if existente == None:
        return None
    if id_antigo != id_novo:
        colisao = localizar(id_novo)
        if colisao != None:
            raise UsuarioJaExiste()
    log = Log(existente)
    atualizar_dao(id_antigo, id_novo, nome, segredo)
    novo = Usuario(id_novo, nome, segredo)
    log.finalizar(novo)
    return novo
