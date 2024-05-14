from flask import Flask, jsonify, request
from criar_banco import criar_tabela
from banco_de_dados_class import Banco


app = Flask(__name__)

criar_tabela()

conect_db = Banco()


# Obter livros
@app.route('/livros', methods=['GET'])
def obter_livros():
    # Retorne os livros como JSON
    return jsonify(conect_db.carregar_dados())


# Obter livro por id
@app.route('/livros/<int:_id>', methods=['GET'])
def obter_livros_id(_id):
    return jsonify(conect_db.carregar_dados(_id))


# Editar e deletar
@app.route('/livros/<int:_id>', methods=['PUT', 'DELETE'])
def editar_livro_por_id(_id):
    if request.method == 'PUT':
        livro_alterado = request.get_json()
        conect_db.editar_dados(_id, livro_alterado)
        return jsonify(conect_db.carregar_dados(_id))

    if request.method == 'DELETE':
        a = conect_db.deletar_dados(_id)
        return jsonify(a)


# Adicionar
@app.route('/livros', methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    verificar_se_existe = conect_db.carregar_dados(variavel_id=None, nome_do_livro=novo_livro['livro'])
    if verificar_se_existe != 1:
        conect_db.adicionar_dados(novo_livro)
        return jsonify("Livro adicionado")
    else:
        return jsonify("Livro já está adicionado")


app.run(port=5000, host='localhost', debug=True)
