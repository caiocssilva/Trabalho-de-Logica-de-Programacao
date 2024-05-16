#Questão 2 

# Mensagem de boas vindas 
print("Bem Vindo a Loja de Gelados do Caio César")

# Apresenta um "layout" em forma de Menu ao usuário
print("-" * 20, "CARDÁPIO", "-" * 20)
print("-" * 50)
print("-" * 5, "|", "TAMANHO", "|", "CUPUAÇU (CP)", "|", "AÇAÍ (AC)", "|", "-" * 5)
print("-" * 5, "|", " " * 2, "P", " " * 2,  "|", " " * 1, "R$ 9,00", " " * 2, "|",  "R$ 11,00", " |", "-" * 5)
print("-" * 5, "|", " " * 2, "M", " " * 2,  "|", " " * 1, "R$ 14,00", " " * 1, "|",  "R$ 16,00", "" * 1, "|", "-" * 5)
print("-" * 5, "|", " " * 2, "G", " " * 2,  "|", " " * 1, "R$ 18,00", " " * 1, "|",  "R$ 20,00", "" * 1, "|", "-" * 5)
print("-" * 50)

# Variável para controlar o total do pedido
total_pedido = 0

# Variáveis para armazenar o valor dos tamanhos dos produtos
preco_cp_p = 9
preco_cp_m = 14
preco_cp_g = 18

preco_ac_p = 11
preco_ac_m = 16
preco_ac_g = 20

# Loop principal para solicitar pedidos ao cliente
while True:
    sabor = input("Entre com o sabor desejado (CP/AC): ").upper()

    if sabor == 'CP' or sabor == 'AC':
        # Solicita o tamanho
        tamanho = input("Entre com o tamanho desejado (P/M/G): ").upper()

        if tamanho in ("P", "M", "G"):
            if sabor == 'CP':
                if tamanho == "P":
                    print(f"Você pediu um Cupuaçu no tamanho {tamanho}: R$ {preco_cp_p:.2f}")
                    total_pedido += preco_cp_p
                elif tamanho == "M":
                    print(f"Você pediu um Cupuaçu no tamanho {tamanho}: R$ {preco_cp_m:.2f}")
                    total_pedido += preco_cp_m
                else:
                    print(f"Você pediu um Cupuaçu no tamanho {tamanho}: R$ {preco_cp_g:.2f}")
                    total_pedido += preco_cp_g
            else:
                if tamanho == "P":
                    print(f"Você pediu um Açaí no tamanho {tamanho}: R$ {preco_ac_p:.2f}")
                    total_pedido += preco_ac_p
                elif tamanho == "M":
                    print(f"Você pediu um Açaí no tamanho {tamanho}: R$ {preco_ac_m:.2f}")
                    total_pedido += preco_ac_m
                else:
                    print(f"Você pediu um Açaí no tamanho {tamanho}: R$ {preco_ac_g:.2f}")
                    total_pedido += preco_ac_g
        # Se o tamanho for inválido, apresenta uma mensagem e volta ao loop
        else:
            print("Tamanho inválido. Tente novamente. \n")
            continue
    # Se o sabor for inválido, apresenta uma mensagem e volta ao loop
    else:
        print("Sabor inválido. Tente novamente. \n")
        continue
    print()
    adicional = input("Deseja pedir mais alguma coisa? (S/N):").upper()

    if adicional != 'S':
        break

print()
print(f"O valor total a ser pago: R$ {total_pedido:.2f}")