hora = input('Digite um valor de hora: ')

if hora.isnumeric():
    hora = int(hora)
    if hora >= 0 and hora <= 11:
        print('Bom dia!')
    elif hora > 11 and hora <= 17:
        print('Boa tarde!')
    elif hora > 17 and hora <= 23:
        print('Boa noite!')
    else:
        print('"Hora" precisa ser um valor entre 0 e 23.')

else:
    print('Não é um valor de hora válido!')