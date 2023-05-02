nome = "Fulano"
idade = 55
altura = 1.75
peso = 93
ano_atual = 2022

ano_nascimento = ano_atual - idade
imc = peso / altura**2

print(f'{nome} nasceu em {ano_nascimento}, portanto no ano atual de {ano_atual}, ele tem {idade} anos de idade.')
#print('A altura de {} é de {:.2f} e seu peso é de {}kg.'.format(nome, altura, peso))
print(f'A altura de {nome} é de {altura:.2f} e seu peso é de {peso}')
#print('O IMC de {} é de {:.2f}.'.format(nome, imc))
print(f'O IMC de {nome} é de {imc:.2f}.')