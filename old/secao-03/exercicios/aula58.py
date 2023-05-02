# Exercício 1
# def funcao1(funcao2):
#     # print('Entrou na função 1')
#     return funcao2()
#
#
# def funcao2():
#     # print('Entrou na função 2')
#     var = 'valor'
#     return(var)
#
#
# print(funcao1(funcao2))

# Exercício 2
#
# def funcao1(funcao2):
#     # print('Entrou na função 1')
#     saudacao('Olá', 'Fulano')
#     soma(4, 3, 3)
#
#     return funcao2()
#
#
# def funcao2():
#     # print('Entrou na função 2')
#     var = 'valor'
#     return(var)
#
#
# def saudacao(saudacao, nome):
#     print(f'{saudacao}, {nome}.')
#
#
# def soma(n1, n2, n3):
#     print(n1+n2+n3)
#
#
# print(funcao1(funcao2))
"""
Solução junto com a aula
"""


# Exercício 01
#
# def ola_mundo():
#     return 'Olá mundo!'
#
#
# def mestre(funcao):
#     return funcao()
#
#
# executando = mestre(ola_mundo)
# print(executando)


# Exercício 02




def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def fala_oi(nome):
    return f'Oi, {nome}.'


def saudacao(saudacao, nome):
    return f'{saudacao}, {nome}.'


executando = mestre(fala_oi, 'Luiz')
executando2 = mestre(saudacao, 'Bom dia', 'Luiz')
executando3 = mestre(saudacao, 'Opa', nome='João')

print(executando)
print(executando2)
print(executando3)











