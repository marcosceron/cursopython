nome = 'Marcos Gonçalves'
idade = 33
altura = 1.80
e_maior = idade > 18
peso = 80
imc = peso / altura**2

#print(nome, 'tem', idade, 'anos de idade e seu IMC é de', imc)
print(f'{nome} tem {idade} anos de idade e seu IMC é de {imc:.2f}')
print('{} tem {} anos de idade e seu IMC é de {:.2f}'.format(nome, idade, imc))
print('{2} {0} {0} tem {1} anos e seu IMC é de {2}'.format(nome, idade, imc))

print('{n} tem {i} anos de idade e seu IMC é de {im}'.format(n=nome, i=idade, im=imc))