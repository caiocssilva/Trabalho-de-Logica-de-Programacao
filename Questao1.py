#Questão 1 - APP de vendas

# Saudação
print('Bem-vindo a Loja do Caio César')

# Solicita o valor do produto e a quantidade
preco = float(input('Entre com o valor do produto: '))
quantidade = int(input('Entre com a quantidade do produto: '))

# Armazena o valor total da compra
total = preco * quantidade

# Armazena os valores dos descontos a serem aplicados
desconto_4 = ((total * 4) / 100) 
desconto_7 = ((total * 7) / 100) 
desconto_11 = ((total * 11) / 100) 

# Validação do desconto
if total < 2500:
    # Desconto 0%
    print(f"O Valor SEM desconto: R${total:.2f}")
    
elif total < 6000:
    # Desconto 4%;
    print(f"O Valor SEM desconto: R${total:.2f}")
    print(f"O Valor COM desconto: R${total - desconto_4:.2f}")

elif total < 10000:
    # Desconto de 7%
    print(f"O Valor SEM desconto: R${total:.2f}")
    print(f"O Valor COM desconto: R${total - desconto_7:.2f}")
else:
    # Desconto 11%
    print(f"O Valor SEM desconto: R${total:.2f}")
    print(f"O Valor COM desconto: R${total - desconto_11:.2f}")