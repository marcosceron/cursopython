
# def funcao(arg, arg2):
#     return arg * arg2
#
#
# var = funcao(2, 2)
# print(var)

# a = lambda x, y: x * y

# lista = [
#     ['P1', 13],
#     ['P2', 6],
#     ['P3', 7],
#     ['P4', 50],
#     ['P5', 8],
# ]
#
# print('Lista antes: ', lista)
# lista.sort(key=lambda i: i[1])
# print(lista.sort(key=lambda i: i[1]))
# print('Lista depois do sort: ', lista)
#
# def func(item):
#     return item[1]

# print('Lista sem lambda')
# print(sorted(lista, key=func))
#
# print('#####')
#
# print('Lista com lambda')
# print(sorted(lista, key=lambda i: i[0], reverse=True))
# print(lista)

# lista2 = [
#     [7, 'Renato'],
#     [1, 'Danrlei'],
#     [3, 'Geromel'],
#     [9, 'Jardel'],
# ]
#
# print('Lista antes', lista2)
# l = sorted(lista2, key=lambda x: x[0])
# print('Lista com sorted', l)
# print('Lista depois', lista2)
#

def calcular_imposto(preco):
    return preco * 0.3

precos = [100, 500, 10, 25]

impostos = list(map(calcular_imposto, precos))
print(impostos)


impostos_2 = list(map(lambda x: x*0.3, precos))
print(impostos_2)
