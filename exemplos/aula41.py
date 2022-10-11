"""
Split, Join, Enumerate em Python
* Split - Dividir uma string # str
* Join - Juntar uma lista # str
* Enumerate - Enumarar elementos da lista # iteráveis
"""

string = "O Brasil é o país do futebol, o Brasil é penta."
lista_1 = string.split(' ')
lista_2 = string.split(',')

# palavra = ''
# contagem = 0
# #laco = 0
# for valor in lista_1:
#     qtd_vezes = lista_1.count(valor)
#     #print(f'Laço: {laco} - qtd_vezes = {qtd_vezes} - palavra = "{valor}"')
#     #laco += 1
#
#     if qtd_vezes > contagem:
#         contagem = qtd_vezes
#         palavra = valor
#         #print(f'   Entrou no if - contagem = {contagem}')
#
# print(f'A palavra que apareceu mais vezes é "{palavra}" ({contagem}x)')
#
# for valor in lista_2:
#     print(valor.strip().capitalize())

# lista = ['O', 'Brasil', 'é', 'Penta.']
# string = ','.join(lista)
#
# print(string)


# string = 'O Brasil é penta.'
# lista = string.split(' ')
#
# for indice, valor in enumerate(lista):
#     print(indice, valor, lista[indice])

lista = ['Luiz', 'João', 'Maria']

n1, n2, n3 = lista

print(n2)

for indice, nome in enumerate(lista):
    print(indice, nome)