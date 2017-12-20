import sqlite3

class UsuarioDAO():
    def __init__(self):
        pass

    def inserir(self, usuario):
        try:
            conn = sqlite3.connect('Rede_Social.db')
            cursor = conn.cursor()

            cursor.execute("""
               INSERT INTO usuario(nome,email,senha,nascimento,profissao,genero,cidade,estado,pais)
               VALUES(?,?,?,?,?,?,?,?,?)
            """, usuario.nome, usuario.email, usuario.senha, usuario.nascimento, usuario.profissao, usuario.genero, usuario.cidade, usuario.estado, usuario.pais)

            conn.commit()
            cursor.close()

        except Exception as err:
            print(err)



    def atualizar(self):
        pass

    def deletar(self):
        pass
    
    def listar(self):
        pass
