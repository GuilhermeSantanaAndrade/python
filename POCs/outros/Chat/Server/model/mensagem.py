from infra.db import con
from wrap_connection import transact
from model.mensagem import Mensagem

sql_criar = "INSERT INTO Mensagens(id, id_remetente, id_destinatario, texto) VALUES (?, ?, ?, ?)"
sql_listar = "SELECT id, id_remetente, id_destinatario, texto FROM Mensagens"
sql_localizar = "SELECT id, id_remetente, id_destinatario, texto FROM Mensagens WHERE id = ?"
sql_apagar = "DELETE FROM Mensagens WHERE id = ?"
sql_atualizar = "UPDATE Mensagens SET id = ?, id_remetente = ?, id_destinatario = ?, texto = ? WHERE id = ?"

class MensagemJaExiste(Exception):
    pass

@transact(con)
def listar():
    cursor.execute(sql_listar)
    resultado = []
    for r in cursor.fetchall():
        resultado.append(Mensagem(r[0], r[1], r[2], r[3]))
    return resultado

@transact(con)
def localizar(id):
    cursor.execute(sql_localizar, (id,))
    r = cursor.fetchone()
    if r == None:
        return None
    return Mensagem(r[0], r[1], r[2], r[3])

@transact(con)
def criar(aluno):
    cursor.execute(sql_criar, (Mensagem.id, Mensagem.id_remetente, Mensagem.id_destinatario, Mensagem.texto))
    connection.commit()

@transact(con)
def remover(id):
    cursor.execute(sql_apagar,(id,))
    connection.commit()

@transact(con)
def atualizar(id_antigo, id_novo, id_destinatario, id_remetente, texto):
    cursor.execute(sql_atualizar, (id_novo, id_destinatario, id_remetente, texto))
    connection.commit()