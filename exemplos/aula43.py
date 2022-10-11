"""
Desempacotamento de Listas em Python
"""
lista = ['Luiz', 'João', 'Maria', 'teste', 1,2,3, 'saideira']
n1, n2, n3, *outra_lista, ultimo_da_lista = lista

print(n1, n2)
print(outra_lista)
print(ultimo_da_lista)