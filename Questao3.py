#Questão 3

# Função que verifica o serviço escolhido
def escolha_servico(pergunta):

    print("""
    Entre com o tipo de serviço desejado:\n
    DIG - Digitalização
    ICO - Impressão Colorida
    IPB - Impressão Preto e Branco
    FOT - Fotocópia
    """)
    print()

    # Enquando o usuário não informar uma das opções, ele fica preso no loop
    while True:
        p = input(pergunta).upper();

        # Será validado uma das opções abaixo
        if p == "DIG" or p == "ICO" or p == "IPB" or p == "FOT":
            if p == "DIG":
                return valor_digitalizacao
            elif p == "ICO":
                return valor_impressao_colorida
            elif p == "IPB":
                return valor_impressao_preto_branco
            else:
                return valor_fotocopia
            break
        # Se a opção for diferente das apresentadas, solicita novamente um serviço
        else:
            print()
            print('Escolha inválida, entre com o tipo do serviço novamente \n')
            print("""
    Entre com o tipo de serviço desejado:\n
    DIG - Digitalização
    ICO - Impressão Colorida
    IPB - Impressão Preto e Branco
    FOT - Fotocópia
            """)
            print()
            continue

# Função que recebe e retorna o número de páginas
def num_paginas(pergunta):
    """
    Essa função solicita ao usuário um número o número de páginas.
    Ela garante que o usuário informe exatamente a opção correta.

    pergunta    :   string;
    return      :   opção escolhida;
    """

    # Enquanto o usuário não informar uma das opções, ele fica preso no loop
    while True:

        # Realizamos a tratativa de possíveis erros com (TRY / EXCEPT)
        try:
            # Solicita ao usuário um número de páginas
            # Verifica se o valor informado se enquadra em um dos critérios
            paginas = int(input(pergunta))

            # Não permite valores menores que 0 e nem maiores que 20.000
            # Se o valor estiver fora do intervalo, retoma a pergunta
            if paginas <= 0 or paginas >= 20000:
                print("Não aceitamos pedidos menor que 1 ou acima de 20.000 páginas.\n\n")
                continue

            # Menos de 20 páginas - Não tem desconto
            if paginas < 20:
                return paginas * servico_escolhido_cliente

            # Menos de 200 páginas - Desconto de 15%
            elif paginas < 200:
                valor = paginas * servico_escolhido_cliente
                desconto = valor - ((valor * 15) / 100)
                return desconto

            # Menos de 2000 páginas - Desconto de 20%
            elif paginas < 2000:
                valor = paginas * servico_escolhido_cliente
                desconto = valor - ((valor * 20) / 100)
                return desconto

            # Menos de 20000 páginas - Desconto de 25%
            elif paginas < 20000:
                valor = paginas * servico_escolhido_cliente
                desconto = valor - ((valor * 25) / 100)
                return desconto

            # Sai do loop
            break

        # Se valor informado for inválido, retorna à pergunta
        except:
            print("Valor inválido. Tente novamente.\n")

# Função que verifica se deseja servico extra e retorna o escolhido
def servico_extra(pergunta):
    """
        Essa função verifica se o usuário deseja servico extra.

        pergunta    :   string
        return      :   opção escolhida
    """

    # Enquanto o usuário não informar uma das opções, ele fica preso no loop
    while True:

        # Realizamos a tratativa de possíveis erros com (TRY / EXCEPT)
        try:

            # Solicita ao usuário qual serviço extra deseja
            # Verifica se o valor informado se enquadra em um dos critérios
            escolha = int(input(pergunta))

            # Se Encadernação Simples - 15 reais
            if escolha == 1:
                valor = 15
                return valor

            # Se Encadernação Capa Dura - 40 reais
            elif escolha == 2:
                valor = 40
                return valor

            # Finaliza o programa
            elif escolha == 0:
                return 0
                break

            # Se a escolha não for uma das opções oferecidas
            else:
                print("Valor inválido. Tente novamente.\n")

        # Caso apresente algum erro de validação com o valor informado
        except:
            print("Escolha uma das opções apresentadas.\n")

# Variáveis que armazena o valor dos serviços oferecidos
valor_digitalizacao = 1.10
valor_impressao_colorida = 1
valor_impressao_preto_branco = 0.40
valor_fotocopia = 0.20

# PROGRAMA PRINCIPAL

# Mensagem de boas vindas com o nome
print(f"    Bem vindo a Copiadora do Caio\n")

# Serviço Escolhido pelo cliente recebe o serviço desejado
servico_escolhido_cliente = escolha_servico("Qual serviço deseja realizar? ")

# Total de Páginas recebe a quantidade páginas
total_paginas = num_paginas("Informe o número de páginas: ")

# Extra recebe se o cliente deseja algum serviço extra
extra_cliente = servico_extra("""Deseja adicionar algum serviço extra:\n
    1 - Encadernação Simples - R$ 15.00
    2 - Encadernação Capa Dura - R$ 40.00
    0 - Não desejo mais nada \n""")

# Mostra o valor total dos serviços ao final do programa
print(f"Total do serviço: R$ {total_paginas + extra_cliente:.2f} (Serviço: {total_paginas:.2f} + extra: {extra_cliente:.2f})")