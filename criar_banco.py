import sqlite3


def criar_tabela():
    banco = sqlite3.connect('dados_dos_livros.db')
    cursor = banco.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='livros'")
    if cursor.fetchone() is None:
        cursor.execute("CREATE TABLE livros ("
                       "id INTEGER PRIMARY KEY,"
                       " livro TEXT,"
                       " autor TEXT )")

    banco.commit()

    banco.close()


if __name__ == '__main__':
    criar_tabela()
