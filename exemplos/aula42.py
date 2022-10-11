"""
* Enumarete - Enumerar elementos da lista # list
"""
lista = [
    # 0      1       2
    ['Edu', 'João', 'Luiz'],     # 0
    ['Maria', 'Aline', 'Joana'], # 1
    ['Helena', 'Paula', 'Lu'],   # 2
]

for v1 in enumerate(lista, 53):
    valor_enumerado, minha_lista = v1
    print(valor_enumerado, minha_lista)
    n1, n2, n3 = minha_lista
    print(n1, n3)