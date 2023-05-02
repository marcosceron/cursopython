"""
For / Else em Python
"""
lista = ['Abelardo', 'João', 'Maria']

for valor in lista:
    if valor.lower().startswith('j'):
        break
else:
    print('Não existe uma palavra que começa com J.')