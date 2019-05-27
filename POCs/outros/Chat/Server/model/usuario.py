class Usuario():
    def __init__(self, id, nome, segredo):
        self.__id = id
        self.__nome = nome
        self.__segredo = segredo

    def atualizar(self, id, nome, segredo):
        self.__id = id
        self.__nome = nome
        self.__segredo = segredo
        return self

    @property
    def id(self):
        return self.__id

    @property    
    def nome(self):
        return self.__nome

    @property    
    def segredo(self):
        return self.__segredo        
