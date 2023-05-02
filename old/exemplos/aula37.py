"""
For in Python
Iterando strings com for
Função range(start=0, stop, step=1)
"""

# for n in range(20, 10, -1):
#     print(n)

# for n in range(0, 100, 8):
#     print(n)
#
# print('#######')
#
# for n in range(100):
#     if n % 8 == 0:
#         print(n)

texto = 'Python'
nova_string = ''

# continue - pula para o próximo laço
# break - termina o laço

for letra in texto:
    if letra == 't':
        continue
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
        break
    else:
        nova_string += letra

print(nova_string)