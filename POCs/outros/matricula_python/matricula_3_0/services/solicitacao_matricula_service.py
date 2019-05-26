from model.solicitacao_matricula import Solicitacao_matricula
from infra.log import Log

solicitacao_matriculas_db = []

class Solicitacao_matriculaJaExiste(Exception):
    pass

class DataInvalida(Exception):
    pass

class AlunoNaoExiste(Exception):
    pass

class CoordenadorNaoExiste(Exception):
    pass

class DisciplinaOfertadaNaoExiste(Exception):
    pass

class StatusInvalido(Exception):
    pass

def listar():
    return solicitacao_matriculas_db

def localizar(id):
    for x in solicitacao_matriculas_db:
        if x.id == id:
            return x
    return None


def validar_data(sdata):
    import datetime

    try:
        data = datetime.datetime.strptime(sdata, "%d/%m/%Y")
    except:
        return False
    else:
        return True

def validaStatus(status):
    if status >=1 and status <=6:
        return True
    else:
        return False

def criar(id, id_aluno, id_disciplina_ofertada, dt_solicitacao, id_coordenador, status):
    from services.alunos_service import localizar as localizar_alunos
    from services.coordenador_service import localizar as localizar_coordenador
    from services.disciplina_ofertada_service import localizar as localizar_disciplina_ofertada
    if not validar_data(dt_solicitacao):
        raise DataInvalida()
    if not validaStatus(status):
        raise StatusInvalido()
    if localizar(id) != None:
        raise Solicitacao_matriculaJaExiste()
    if localizar_alunos(id_aluno) == None:
        raise AlunoNaoExiste()
    if localizar_coordenador(id_coordenador) == None:
        raise CoordenadorNaoExiste()
    if localizar_disciplina_ofertada(id_disciplina_ofertada) == None:
        raise DisciplinaOfertadaNaoExiste()
    log = Log(None)
    criado = Solicitacao_matricula(id, id_aluno, id_disciplina_ofertada, dt_solicitacao, id_coordenador, status)
    solicitacao_matriculas_db.append(criado)
    log.finalizar(criado)
    return criado

def remover(id):
    existente = localizar(id)
    if existente == None:
        return None
    log = Log(existente)
    solicitacao_matriculas_db.remove(existente)
    log.finalizar(None)
    return existente

def atualizar(id_antigo, id_novo, id_aluno, id_disciplina_ofertada, dt_solicitacao, id_coordenador, status):
    from services.alunos_service import localizar as localizar_alunos
    from services.disciplina_ofertada_service import localizar as localizar_disciplinaOfertada
    from services.coordenador_service import localizar as localizar_coordenador
    if not validar_data(dt_solicitacao):
        raise DataInvalida()
    if not validaStatus(status):
        raise StatusInvalido()
    existente = localizar(id_antigo)
    if existente == None:
        return None
    if id_antigo != id_novo:
        colisao = localizar(id_novo)
        if colisao != None:
            raise Solicitacao_matriculaJaExiste()
    if localizar_alunos(id_aluno) == None:
        raise AlunoNaoExiste()
    if localizar_disciplinaOfertada(id_disciplina_ofertada) == None:
        raise DisciplinaOfertadaNaoExiste()
    if localizar_coordenador(id_coordenador) == None:
        raise CoordenadorNaoExiste()

    log = Log(existente)
    existente.atualizar(id, id_aluno, id_disciplina_ofertada, dt_solicitacao, id_coordenador, status)
    log.finalizar(existente)
    return existente