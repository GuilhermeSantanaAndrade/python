class Disciplina():
    def __init__(self, id, nome, status, plano_ensino, carga_horaria, id_coordenador):
        self.__id = id
        self.__nome = nome
        self.__status = status
        self.__plano_ensino = plano_ensino
        self.__carga_horaria = carga_horaria
        self.__id_coordenador = id_coordenador

    def atualizar(self, id, nome, status, plano_ensino, carga_horaria, id_coordenador):
        self.__id = id
        self.__nome = nome
        self.__status = status
        self.__plano_ensino = plano_ensino
        self.__carga_horaria = carga_horaria
        self.__id_coordenador = id_coordenador
        return self

    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome
		
    @property
    def status(self):
        return self.__status
		
    @property
    def plano_ensino(self):
        return self.__plano_ensino
		
    @property
    def carga_horaria(self):
        return self.__carga_horaria
		
    @property
    def id_coordenador(self):
        return self.__id_coordenador		