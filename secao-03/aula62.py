#
# d1 = {'chave1': 'valor da chave'}
# d1['nova_chave'] = 'Valor da nova chave'
#
# print(d1)
# print(d1['chave1'])
#
# d1 = dict(chave1='Valor da chave', chave2='Valor da outra chave')
# d1['nova_chave'] = 'Valor da nova chave'

#
# d1 = {
#     'str': 'valor',
#     123: 'Outro valor',
#     (1,2,3,4): 'Tupla',
# }

# del d1['str']
#
# print(d1)

# d1.update({'nova_chave': 'novo_valor'})
#
# d1['nova_chave'] = 'Agora ela existe'
#
# if d1.get('nova_chave') is not None:
#     print(d1.get('nova_chave'))
#
# print(123)

#
# print('str' in d1)
# print('str' in d1.keys())
# print('valor' in d1.values())

# print(len(d1))
#
# d2 = {
#     'chave1': 'valor',
#     'chave2': 'outro valor',
#     'chave3': 'Tupla',
# }
#
# for k, v in d2.items():
#     print(k, v)

# clientes = {
#     'cliente1' : {
#         'nome': 'Luiz',
#         'sobrenome': 'Otávio',
#     },
#     'cliente2': {
#         'nome': 'João',
#         'sobrenome': 'Moreira',
#     },
#     'cliente3': {
#         'nome': 'Ramon',
#         'sobrenome': 'Valdez',
#     },
# }
#
#
# for clientes_k, clientes_v in clientes.items():
#     print(f'Exibindo {clientes_k}')
#     for dados_k, dados_v in clientes_v.items():
#         print(f'\t{dados_k} = {dados_v}')

#
# d1 = {1: 'a', 2: 'b', 3: 'c'}
# v = d1
#
# v[1] = 'Clotilde'
#
# print(d1)
# print(v)


# d1 = {1: 'a', 2: 'b', 3: 'c', 'd': ['Florinda', 'Furtado']}
# v = d1.copy()
#
# v[1] = 'Clotilde'
#
# v['d'][0] = 'Joãozinho'
# v[3] = 'C cedilha'
#
# print(d1)
# print(v)

# import copy
#
# d1 = {1: 'a', 2: 'b', 3: 'c', 'd': ['Florinda', 'Furtado']}
# v = copy.deepcopy(d1)
#
# v[1] = 'Clotilde'
# v['d'][0] = 'Joãozinho'
#
# print(d1)
# print(v)

#
# d1 = {1: 'a', 2: 'b', 3: 'c', 'd': ('Florinda', 'Furtado')}
# v = d1.copy()
#
# v[1] = 'Clotilde'
# v['d'] = ('Marcos', 'Ceron')
#
# print(d1)
# print(v)

# lista = [
#     ['c1', 1],
#     ['c2', 2],
#     ['c3', 3],
# ]
#
#
# lista2 = (
#     ('c1', 1),
#     ('c2', 2),
#     ('c3', 3),
# )
#
#
# d1 = dict(lista)
# d2 = dict(lista2)
#
# print(d1)
# print(d2)
# print(d1['c3'])

d1 = {
    1: 'a',
    2: 'b',
    3: 'c',
}


d2 = {
    4: 'd',
    5: 'e',
}

# d1.popitem()
print(d1)
print(d2)

d1.update(d2)
print(d1)
