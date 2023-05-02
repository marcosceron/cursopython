"""
While
contadores
acumuladores
"""
contador = 1
acumulador = 1

while contador <= 10:
    if contador > 5:
        break

    print(contador, acumulador)


    acumulador = acumulador + contador
    contador += 1
else:
    print('Cheguei no else.')
print('Isso será executado.')