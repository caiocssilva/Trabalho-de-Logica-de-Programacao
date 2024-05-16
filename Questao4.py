#Questão 4

# Boas vindas com o nome

print("Bem vindo a Livraria do Caio César")

# Função que cadastra livros recebendo como parâmetro ID
def cadastrar_novo_livro(identificador):
    """
    Essa função realiza o cadastro de um livro, recebendo como parâmetro
    um ID auto incrementável e solicita ao usuário:
    Nome, Autor, Editora e armazena esses valores em um dicionário. Ao final,
    retorna o dicionário com os respectivos valores.

    :identificador      :   número único recebido como parâmetro
    :return  :   retorna o dicionário;
    """

    # Print um "layout" de menu ao usuário
    print("-" * 50)
    print("-" * 14, "MENU CADASTRAR LIVRO", "-" * 14)
    print()

    # Definimos um identificador global para ser incrementado a cada novo cadastro
    global identificador_global

    # Solicita ao usuário as informações do livro
    identificador = int(identificador_global) + 1
    print(f"ID do Livro: {identificador}")
    nome = input("Nome do LIVRO: ").upper()
    autor = input("Nome do AUTOR: ").upper()
    editora = input("Nome da EDITORA: ").upper()
    identificador_global += 1

    # Cadastros inseridos em dicionários e incluído em lista
    livro = {"ID": identificador, "NOME": nome, "AUTOR": autor, "EDITORA": editora}

    print()

    # Retorna o dicionário para ser incluído na lista
    return livro

# Função que consulta livros cadastrados
def consultar_livro():
    """
    Essa função verifica qual o tipo de consulta o usuário deseja fazer na
    livraria e valida as opções, retornando assim a opção desejada.
    """

    # # Apresenta um "layout" de Menu ao usuário
    # print("-" * 50)
    # print("-" * 14, "MENU CONSULTAR LIVRO", "-" * 14)

    # Apresenta ao usuário o menu com as informações de consultar os livros
    while True:
        try:
            # Apresenta um "layout" de Menu ao usuário
            print("-" * 50)
            print("-" * 14, "MENU CONSULTAR LIVRO", "-" * 14)
            print()

            ec = int(input("""
            1 - Consultar Todos os Livros
            2 - Consultar Livro por ID
            3 - Consultar Livro(s) por Autor
            4 - Retornar ao Menu\n\n
            """))

            # Opção para consultar TODOS os livros
            if ec == 1:
                if lista_livros == []:
                    print("Não foi cadastrado nenhum livro.")
                    break
                else:
                    for nome in lista_livros:
                        print(f"{nome['ID']}º Livro:")
                        print(f"ID: {nome['ID']}")
                        print(f"NOME: {nome['NOME']}")
                        print(f"AUTOR: {nome['AUTOR']}")
                        print(f"EDITORA: {nome['EDITORA']}")
                        print()

            # Opção para consultar o livro pelo seu ID
            elif ec == 2:

                # Verifica se a lista está vazia antes de prosseguir
                if lista_livros == []:
                    print("Não foi cadastrado nenhum livro.")
                    break

                escolha = int(input("Informe o ID do livro que deseja consultar: "))

                if escolha <= 0 or escolha > len(lista_livros):
                    print("Não existe nenhum livro com esse ID.")

                for id in lista_livros:
                    if escolha == id["ID"]:
                        print(f"ID: {id['ID']}")
                        print(f"NOME: {id['NOME']}")
                        print(f"AUTOR: {id['AUTOR']}")
                        print(f"EDITORA: {id['EDITORA']}")

            # Opção para consultar o(s) livro(s) pelo seu AUTOR
            elif ec == 3:

                # Verifica se a lista está vazia antes de prosseguir
                if lista_livros == []:
                    print("Não foi cadastrado nenhum livro.")
                    break

                # Solicita um autor ao usuário
                escolha = input("Qual autor deseja consultar? ").upper()

                # Inicia a variável como FALSE para realizar o controle
                livro_encontrado = False

                # Faz uma varredura dentro da lista de livros passando
                # cada um dos dicionários de livros existentes
                for livro in lista_livros:

                    # A cada iteração se a escolha for igual ao autor, mostra ao
                    # usuário, os livros daquele autor
                    if escolha == livro["AUTOR"]:
                        print(f"ID: {livro['ID']}")
                        print(f"NOME: {livro['NOME']}")
                        print(f"AUTOR: {livro['AUTOR']}")
                        print(f"EDITORA: {livro['EDITORA']}")
                        print()

                        # Ao encontrar, muda a variável de controle para TRUE
                        livro_encontrado = True

                # Se não houver nenhum livro encontrado, a variável permanece
                # como FALSE e apresenta a mensagem ao usuário
                if not livro_encontrado:
                    print("Não existe nenhum livro desse autor.")

            # Retorna ao Menu Principal
            elif ec == 4:
                break

            # Se o usuário informar algum valor que não esteja entre as opções
            else:
                print("Opção inválida. Tente novamente.\n")

        # Tratamento de exceção para caso o usuário digite um valor inválido
        except:
            print("Valor inválido. Tente novamente.\n")

# Função que remove livro da lista
def remover_livro():
    """
    Essa função realiza a remoção de um livro. No código é solicitado
    um ID para realizar a remoção e se for encontrado, solicita ao usuário
    a confirmação para deleção do livro. Se não encontrar, informa ao usuário
    que não encontrou nenhum livro com aquele ID.
    """

    # Apresenta um "layout" de Menu ao usuário
    print("-" * 50)
    print("-" * 15, "MENU REMOVER LIVRO", "-" * 15)
    print()

    while True:
        try:
            # Verifica se a lista de livros está vazia
            if not lista_livros:
                print("Não foi cadastrado nenhum livro.")
                break

            # Solicita ao usuário o ID do livro que ele deseja remover
            er = int(input("Deseja remover o livro com qual ID: "))

            # Inicia a variável como FALSE para realizar o controle
            id_encontrado = False

            if er <= 0 or er > len(lista_livros):
                print("ID Inválido. Por favor, insira um ID válido.")
                print()
                continue

            # Varre a lista de livros em busca do ID informado
            for id in lista_livros:
                # Se encontra o ID fornecido, mostra uma mensagem de confirmação
                if er == id["ID"]:
                    id_encontrado = True
                    escolha = input("Tem certeza que deseja excluir esse livro? ").upper()

                    # Se o usuário confirmar, a remoção será realizada
                    if escolha == 'S':
                        lista_livros.remove(id)
                        print(f"Livro {id['NOME']} removido com sucesso.")
                        print()
            if not id_encontrado:
                print("Não existe nenhum livro com esse ID.")
                print()

            # Sai do loop
            break

        # Tratamento de exceção para caso o usuário digite um valor inválido
        except:
            print("Opção inválida. Tente novamente.\n")
            print()
# PROGRAMA PRINCIPAL

# Declarando variável global e lista vazia
lista_livros = []
identificador_global = 0

# Estrutura de Menu fora da função
while True:
        # Apresenta um "layout" de Menu ao usuário
        print("-" * 50)
        print("-" * 17, "MENU PRINCIPAL", "-" * 17)
        print()

        try:
            # Menu Principal com as opções para o usuário
            menu = int(input("""Escolha a opção desejada:
            1 - Cadastrar Livro
            2 - Consultar Livro(s)
            3 - Remover Livro
            4 - Sair \n\n"""))

            # Opção para CADASTRAR novo livro
            if menu == 1:
                novo_livro = cadastrar_novo_livro(identificador_global)

                # Faz uma iteração dentro da lista passando por cada
                # um dos dicionários de livro para verificar se
                # já existe algum livro com o mesmo nome e mesmo autor
                for livro in lista_livros:

                    # Se encontrar, apresenta ao usuário uma mensagem de
                    # que o livro já existe
                    if novo_livro["NOME"] == livro["NOME"] and novo_livro["AUTOR"] == livro["AUTOR"]:
                        print(f"{novo_livro['NOME']} já existe na lista.")

                        # Altera o valor da variável global para -1
                        # Dessa forma o próximo cadastro recebe o número da
                        # sequência de ID
                        identificador_global -= 1

                        # Sai do loop
                        break
                # Se não existir nenhum livro com mesmo nome e autor
                # Realiza o cadastro do novo livro
                else:
                    lista_livros.append(novo_livro)
                    print(f"Livro {novo_livro['NOME']} cadastrado com sucesso.")

            # Opção para CONSULTAR o(s) livro(s) cadastrados
            elif menu == 2:
                consultar_livro()

            # Opção para REMOVER o livro desejado
            elif menu == 3:
                remover_livro()

            # Opção para SAIR do programa
            elif menu == 4:
                print("Programa Finalizado.")
                break
            else:
                print("Opção Inválida. Escolha uma das opções do Menu.\n")
        except:
            print("Valor inválido. Tente novamente.\n")