"""
Funções - def em Python
"""

#
# def divisao(n1, n2):
#     if n2 == 0:
#         return
#
#     return n1 / n2
#
#
# divide = divisao(8,4)
#
# if divide:
#     print(divide)
# else:
#     print('Conta inválida.')

#
# def saudacao(msg='Olá', nome='Usuário'):
#     nome = nome.replace('e', '3')
#     msg = msg.replace('e', '3')
#     return f'{msg}, {nome}.'
#
# variavel = saudacao()
#
# print(variavel)

# def f(var):
#     print(var)
#
# def dumb():
#     return f
#
# # var = dumb()('E colocar o meu valor aqui.')
# var = dumb()
# var('Pode imprimir algo na tela.')

def dumb():
    return ('Luiz', 'Otávio')

var = dumb()
print(var[0], type(var))