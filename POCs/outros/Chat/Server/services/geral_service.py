from model.usuario import Usuario    
from controlador import control
from infra.log import Log
from services.usuario_service import listar as listar_usuarios

def logon(nome, segredo):
    usuarios = listar_usuarios()
    userFound = None
    for usr in usuarios:
        if (usr.nome == nome):
            if (usr.segredo == segredo):
                userFound = usr
                break
            else:
                raise Exception('Senha inválida')
    if (userFound != None):
        print(control.UsuariosOnline)
        usr = Usuario(userFound.id, userFound.nome, userFound.segredo)
        control.pushUsuario(userFound, '127.0.0.1', 5001)
        print(control.UsuariosOnline)
    else:
        raise Exception('Nome de usuário não encontrado')
    return userFound

    