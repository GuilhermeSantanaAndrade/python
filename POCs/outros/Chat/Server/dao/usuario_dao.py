from infra.db import con
from wrap_connection import transact
from model.usuario import Usuario

sql_criar = "INSERT INTO Usuarios(id, nome, segredo) VALUES (?, ?, ?)"
sql_listar = "SELECT id, nome, segredo FROM Usuarios"
sql_localizar = "SELECT id, nome, segredo FROM Usuarios WHERE id = ?"
sql_apagar = "DELETE FROM Usuarios WHERE id = ?"
sql_atualizar = "UPDATE Usuarios SET id = ?, nome = ?, segredo = ? WHERE id = ?"

class UsuarioJaExiste(Exception):
    pass

@transact(con)
def listar():
    cursor.execute(sql_listar)
    resultado = []
    for r in cursor.fetchall():
        resultado.append(Usuario(r[0], r[1], r[2]))
    return resultado

@transact(con)
def localizar(id):
    cursor.execute(sql_localizar, (id,))
    r = cursor.fetchone()
    if r == None:
        return None
    return Usuario(r[0], r[1], r[2])

@transact(con)
def criar(usuario):
    cursor.execute(sql_criar, (usuario.id, usuario.nome, usuario.segredo))
    connection.commit()

@transact(con)
def remover(id):
    cursor.execute(sql_apagar,(id,))
    connection.commit()

@transact(con)
def atualizar(id_antigo, id_novo, nome, segredo):
    cursor.execute(sql_atualizar, (id_novo, nome, segredo, id_antigo))
    connection.commit()