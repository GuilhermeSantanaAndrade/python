class Mensagem():
    def __init__(self, id, id_remetente, id_destinatario, data_hora, texto):
        self.__id = id
        self.__id_remetente = id_remetente
        self.__id_destinatario = id_destinatario
        self.__data_hora = data_hora
        self.__texto = texto

    def atualizar(self, id, id_remetente, id_destinatario, data_hora, texto):
        self.__id = id
        self.__id_remetente = id_remetente
        self.__id_destinatario = id_destinatario
        self.__data_hora = data_hora
        self.__texto = texto
        return self

    @property
    def id(self):
        return self.__id

    @property    
    def id_remetente(self):
        return self.__id_remetente

    @property    
    def id_destinatario(self):
        return self.__id_destinatario

    @property    
    def data_hora(self):
        return self.__data_hora

    @property    
    def texto(self):
        return self.__texto