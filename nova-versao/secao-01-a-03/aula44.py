nome = 'Luiz'
preco = 1000.958976246
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)

print('O hexadecimal de %d é %04x' % (15, 15))

a = 'A'
b = 'B'
c = 1.1
string = 'a={} b={} c={:.2f}'
formato = string.format(a, b, c)

print(formato)