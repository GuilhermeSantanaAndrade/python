from model.usuario import Usuario

class Controlador():
    def __init__(self):
        self.__UsuariosOnline = []
    
    @property
    def UsuariosOnline(self):
        return self.__UsuariosOnline

    def pushUsuario(self, aUsuario, aIP, aPort):
        obj = {"usuario": aUsuario, "IP": aIP, "Port": aPort}
        self.__UsuariosOnline.append(obj)

control = Controlador()