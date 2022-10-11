num = input('Digite um número: ')

try:
    num = int(num)
    if num % 2 == 0:
        print(f'{num} é par.')
    else:
        print(f'{num} é ímpar.')
except:
    print('A entrada informada não é um número inteiro!')
