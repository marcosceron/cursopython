"""
Formatando valores com modificadores

:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(NÚMERO)f - Quantidade de casas decimais (float)
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""
# num_1 = 10
# num_2 = 3
# divisao = num_1 / num_2

# print('{:.2f}'.format(divisao))
# print(f'{divisao:.2f}')
#
# num_1 = 1
# print(f'{num_1:0>10}')
#
# num_2 = 1150
# print(f'{num_2:0>10.2f}')

# nome = 'Otávio Mesquita'
# print(len(nome))
# nome_formatado = '{:@>40}'.format(nome)
# nome_2 = '{n:0<20}'.format(n=nome)

# print(len(nome))
# print(f'{nome:#^50}')

# nome = 'Otávio'
# sobrenome = 'Mesquita'
# nome_formatado = '{0:$>50}\n{1:#<50}'.format(nome, sobrenome)


nome = 'Otávio mesquita DA SiLvA'
#nome = nome.ljust(20, '#')


print(nome.lower())
print(nome.upper())
print(nome.title())
