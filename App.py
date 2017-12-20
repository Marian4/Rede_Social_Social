from Models.Usuario import Usuario
from Database.UsuarioDAO import  UsuarioDAO
import sqlite3

def criarTabelas():
    try:
        conn = sqlite3.connect("Rede_Social.db")
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE usuario(nome varchar(100) primary key, email varchar(100), senha varchar(100),nascimento date,profissao varchar(100),genero varchar(100),cidade varchar(100),estado varchar(100),pais varchar(100))
        """)

    except Exception as err:
        print(err)

def Menu():
    print("MENU: \n"
         "1 - Definir nome da rede social.\n"
         "2 - fazer Login\n"
         "3 - Cadastrar-se\n"
         "0 - Sair")

def main(args = []):

    continuar = True

    while continuar:
        try:
            Menu()
            opcao = int(input("Digite a opção: "))

            if opcao == 1:
                nomeRede = input("Digite o nome da Rede Social:")

            elif opcao == 2:
                #se o usuario estiver o email e senha correspondentes no banco de dados o programa irá exibir as opções da página do Usuario tais como editar perfil, adicionar amigos, excluir amigos.....
                pass
            elif opcao == 3:
                print("Preencha o formulário abaixo:")
                nome = input("Nome:")
                email = input("E-mail:")
                senha = input("Senha:")
                nascimento = input("Nascimento:")
                profissao = input("Profissão:")
                genero = input("Gênero:")
                cidade = input("Cidade:")
                estado = input("Estado:")
                pais = input("País:")
                print()
                usuario = Usuario(nome,email,senha,nascimento,profissao,genero,cidade,estado,pais)
                UsuarioDAO().inserir(usuario)

            elif opcao == 0:
                continuar = False
            else:
                print("Ops! Opção inválida!")

        except ValueError:
            print("Ops! Digite um valor válido")

    print("\nVocê saiu.")

if (__name__ == "__main__"):
    main()
