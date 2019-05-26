class Solicitacao_matricula():
    def __init__(self, id, id_aluno, id_disciplina_ofertada, dt_solicitacao, id_coordenador, status):
        self.__id = id
        self.__id_aluno = id_aluno
        self.__id_disciplina_ofertada = id_disciplina_ofertada
        self.__dt_solicitacao = dt_solicitacao
        self.__id_coordenador = id_coordenador
        self.__status = status

    def atualizar(self, id, id_aluno, id_disciplina_ofertada, dt_solicitacao, id_coordenador, status):
        self.__id = id
        self.__id_aluno = id_aluno
        self.__id_disciplina_ofertada = id_disciplina_ofertada
        self.__dt_solicitacao = dt_solicitacao
        self.__id_coordenador = id_coordenador
        self.__status = status
        return self

    @property
    def id(self):
        return self.__id

    @property
    def id_aluno(self):
        return self.__id_aluno

    @property
    def id_disciplina_ofertada(self):
        return self.__id_disciplina_ofertada

    @property
    def dt_solicitacao(self):
        return self.__dt_solicitacao

    @property
    def id_coordenador(self):
        return self.__id_coordenador

    @property
    def status(self):
        return self.__status