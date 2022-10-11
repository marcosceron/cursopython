"""
Listas em Python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""

# lista = ['A', 'B', 'C', 'D', 'E', 10.5]
# print(lista[::-1])

# l1 = [1,2,3]
# l2 = [4,5,6]
# print(l2)
#
# l2.insert(0, 'banana')
# print(l2)
#
# a = l2.pop()
# print(a)

# l2 = [1,2,3,4,5,6,7,8,9]
#
# print(max(l2))
# print(min(l2))

# print(l2)
#
# l2.insert(0, 'Banana')
# print(l2)
#
# del(l2[0])
# print(l2)


# l2 = [0,1,2,3,4,5,6,7,8,9]
#
# soma = 0
# for valor in l2:
#     soma = soma + valor
#
# print(soma)


# l2 = ['String', True, 10, -20.5]
#
# for elem in l2:
#     print(f'O tipo de elem é {type(elem)} e seu valor é {elem}.')

secreto = 'perfume'
digitadas = []
chances = 3

while chances > 0:
    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Digite apenas uma letra.')
        continue

    digitadas.append(letra)
    if letra in secreto:
        print(f'A letra "{letra}" existe na palavra secreta.')
    else:
        print(f'A letra "{letra}" NÃO existe na palavra secreta.')
        digitadas.pop()
        chances -= 1

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'Fim de jogo! A palavra é "{secreto_temporario}".')
        break
    else:
        print(f'A palavra secreta está assim: "{secreto_temporario}"')

    if chances > 0:
        print(f'Você ainda tem {chances} chances.')
        print()

else:
    print('Você perdeu!')
