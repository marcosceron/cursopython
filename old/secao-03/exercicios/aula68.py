
string = '012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'

# ci = 0
# cf = 10
#
#
# lenght = string.count('0')
# lista = [string[ci:cf] for i in range(lenght)]
#
# string_r = '.'.join(lista)
#
#
# print(lista)
# print(string_r)


# Solução do professor
n = 10
lista = [string[i:i+n] for i in range(0, len(string), n)]
retorno = '.'.join(lista)
print(lista)
print(retorno)
