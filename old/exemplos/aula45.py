"""
Operador ternário em Python
"""
# logged_user = False
# msg = 'Usuário logado.' if logged_user else 'Usuário não logado.'
#
# print(msg)

idade = input('Qual a sua idade? ')

if not idade.isnumeric():
    print('Você precisa digitar apenas números')
else:
    idade = int(idade)
    # e_maior = (idade >= 18)
    msg = 'Pode acessar.' if idade >= 18 else 'Não pode acessar.'

    print(msg)