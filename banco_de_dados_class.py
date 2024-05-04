import sqlite3


class Banco:
    def __init__(self):
        self.db_name = 'dados_dos_livros.db'

    def carregar_dados(self, variavel_id=None):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        if variavel_id is None:
            cursor.execute("SELECT * FROM livros")
        else:
            cursor.execute("SELECT * FROM livros WHERE id=?", (variavel_id,))

        livros = cursor.fetchall()
        conn.close()

        return livros

    def adicionar_dados(self,  novo_livro):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        cursor.execute("INSERT INTO livros (nome, autor) VALUES (?, ?)", (novo_livro['nome'], novo_livro['autor']))
        conn.commit()
        conn.close()

    def editar_dados(self, id_alvo, livro_alterado):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        if livro_alterado['nome'] is not None:
            cursor.execute(""" UPDATE livros SET nome = ? WHERE id = ? """, (livro_alterado['nome'], id_alvo))

        if livro_alterado['autor'] is not None:
            cursor.execute(""" UPDATE livros SET autor = ? WHERE id = ? """, (livro_alterado['autor'], id_alvo))

        conn.commit()
        conn.close()

    def deletar_dados(self, __id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        try:
            cursor.execute("DELETE from livros WHERE id = ?", (__id,))
            conn.commit()
        except sqlite3.Error:
            pass

        conn.close()


if __name__ == '__main__':
    pass
