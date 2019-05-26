class DisciplinaOfertada:
    def __init__(self, id, id_disciplina, id_professor, ano, semestre, turma, id_curso, data):
        self.__id = id
        self.__id_disciplina = id_disciplina
        self.__id_professor = id_professor
        self.__ano = ano
        self.__semestre = semestre
        self.__turma = turma
        self.__id_curso = id_curso
        self.__data = data

    def atualizar(self, id, id_disciplina, id_professor, ano, semestre, turma, id_curso, data):
        self.__id = id
        self.__id_disciplina = id_disciplina
        self.__id_professor = id_professor
        self.__ano = ano
        self.__semestre = semestre
        self.__turma = turma
        self.__id_curso = id_curso
        self.__data = data
        return self

    @property
    def id(self):
        return self.__id

    @property
    def id_disciplina(self):
        return self.__id_disciplina

    @property
    def id_professor(self):
        return self.__id_professor

    @property
    def ano(self):
        return self.__ano

    @property
    def semestre(self):
        return self.__semestre

    @property
    def turma(self):
        return self.__turma

    @property
    def id_curso(self):
        return self.__id_curso

    @property
    def data(self):
        return self.__data