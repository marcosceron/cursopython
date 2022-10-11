"""
Condições IF, ELIF e ELSE
"""
nome = input('Nome: ')
idade = input('Idade: ')

idade = int(idade)

# Limite para pegar empréstimo
limite_inf = 20
limite_sup = 30

if idade >= limite_inf and idade <= limite_sup:
    print(f'{nome} pode pegar o empréstimo.')
else:
    print(f'{nome} NÃO pode pegar o empréstimo.')