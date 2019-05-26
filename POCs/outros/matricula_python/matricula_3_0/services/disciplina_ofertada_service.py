from model.disciplina_ofertada import DisciplinaOfertada
from infra.log import Log

disciplina_ofertada_db = []

class DisciplinaOfertadaJaExiste(Exception):
    pass

class ProfessorNaoExiste(Exception):
    pass

class DataInvalida(Exception):
    pass


class DisciplinaNaoExiste(Exception):
    pass

class CursoNaoExiste(Exception):
    pass

def validar_data(sdata):
    import datetime

    try:
        data = datetime.datetime.strptime(sdata, "%d/%m/%Y")
    except:
        return False
    else:
        return True

def listar():
    return disciplina_ofertada_db

def localizar(id):
    for x in disciplina_ofertada_db:
        if x.id == id:
            return x
    return None

def localizar_colisao(id, id_disciplina, ano, semestre, turma, id_curso):
    for x in disciplina_ofertada_db:
        if x.id != id and \
                x.id_disciplina == id_disciplina and \
                x.ano == ano and \
                x.semestre == semestre and \
                x.turma == turma and \
                x.id_curso == id_curso:
            return x
    return None

def criar(id, id_disciplina, id_professor, ano, semestre, turma, id_curso, data):
    from services.professores_service import localizar as localizar_professor
    from services.disciplina_service import localizar as localizar_disciplina
    from services.curso_service import localizar as localizar_curso
    if not validar_data(data):
        raise DataInvalida()
    if localizar(id) != None:
        raise DisciplinaOfertadaJaExiste()
    if localizar_colisao(id, id_disciplina, ano, semestre, turma, id_curso):
        raise DisciplinaOfertadaJaExiste()
    if localizar_professor(id_professor) == None:
        raise ProfessorNaoExiste()
    if localizar_disciplina(id_disciplina) == None:
        raise DisciplinaNaoExiste()
    if localizar_curso(id_curso) == None:
        raise CursoNaoExiste()
    log = Log(None)
    criado = DisciplinaOfertada(id, id_disciplina, id_professor, ano, semestre, turma, id_curso, data)
    disciplina_ofertada_db.append(criado)
    log.finalizar(criado)
    return criado

def remover(id):
    existente = localizar(id)
    if existente == None:
        return None
    log = Log(existente)
    disciplina_ofertada_db.remove(existente)
    log.finalizar(None)
    return existente

def atualizar(id_antigo, id_novo, id_disciplina, id_professor, ano, semestre, turma, id_curso, data):
    from services.professores_service import localizar as localizar_professor
    from services.disciplina_service import localizar as localizar_disciplina
    from services.curso_service import localizar as localizar_curso

    if not validar_data(data):
        raise DataInvalida()

    existente = localizar(id_antigo)
    if existente == None:
        return None
    if id_antigo != id_novo:
        colisao = localizar(id_novo)
        if colisao != None:
            raise DisciplinaOfertadaJaExiste()

    if localizar_colisao(id_antigo, id_disciplina, ano, semestre, turma, id_curso):
        raise DisciplinaOfertadaJaExiste()
    if localizar_professor(id_professor) == None:
        raise ProfessorNaoExiste()
    if localizar_disciplina(id_disciplina) == None:
        raise DisciplinaNaoExiste()
    if localizar_curso(id_curso) == None:
        raise CursoNaoExiste()


    log = Log(existente)
    existente.atualizar(id_novo, id_disciplina, id_professor, ano, semestre, turma, id_curso, data)
    log.finalizar(existente)
    return existente