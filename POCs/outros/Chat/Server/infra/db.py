import sqlite3

create_sql = ["""
CREATE TABLE IF NOT EXISTS Usuarios (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    segredo TEXT NO NULL
);
""", """
CREATE TABLE IF NOT EXISTS Mensagens (
    id INTEGER PRIMARY KEY,
    id_remetente INTEGER NOT NULL,
    id_destinatario INTEGER NOT NULL,
    data_hora DATE_TIME NOT NULL,
    texto TEXT NOT NULL
);
"""]

remove_sql = ["""
DROP TABLE Usuarios;
""", """
DROP TABLE Mensagens;
"""]

from wrap_connection import transact

def con():
    return sqlite3.connect("chat.db")

@transact(con)
def criar_db():
    for sql in create_sql:
        print(sql)
        cursor.execute(sql)
    connection.commit()

@transact(con)
def remover_db():
    for sql in remove_sql:
        print(sql)
        cursor.execute(sql)
    connection.commit()    