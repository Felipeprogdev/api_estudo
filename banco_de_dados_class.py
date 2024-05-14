import sqlite3


class Banco:
    def __init__(self):
        self.db_name = 'dados_dos_livros.db'

    def carregar_dados(self, variavel_id=None, nome_do_livro=None):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        if variavel_id is not None:
            cursor.execute("SELECT * FROM livros WHERE id=?", (variavel_id,))
        elif nome_do_livro is not None:
            cursor.execute("SELECT * FROM livros WHERE livro LIKE ?", ('%' + nome_do_livro + '%',))
        else:
            cursor.execute("SELECT * FROM livros")

        livros = cursor.fetchall()
        conn.close()

        if nome_do_livro is not None and livros:
            return 1
        else:
            return livros

    def adicionar_dados(self,  novo_livro):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        cursor.execute("INSERT INTO livros (livro, autor) VALUES (?, ?)", (novo_livro['livro'], novo_livro['autor']))
        conn.commit()
        conn.close()

    def editar_dados(self, id_alvo, livro_alterado):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        if livro_alterado['livro'] is not None:
            cursor.execute(""" UPDATE livros SET livro = ? WHERE id = ? """, (livro_alterado['livro'], id_alvo))

        if livro_alterado['autor'] is not None:
            cursor.execute(""" UPDATE livros SET autor = ? WHERE id = ? """, (livro_alterado['autor'], id_alvo))

        conn.commit()
        conn.close()

    def deletar_dados(self, __id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        cursor.execute("DELETE from livros WHERE id = ?", (__id,))
        conn.commit()

        if cursor.rowcount == 0:
            return 'Dado inexistente'
        else:
            return 'Deletado com sucesso!!'

        conn.close()


if __name__ == '__main__':
    pass
