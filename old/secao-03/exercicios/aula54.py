# Exercício 1
def saudacao(saudacao, nome):
    print(f'{saudacao}, {nome}.')


saudacao('Olá', 'Fulano')


# Exercício 2
def soma(n1, n2, n3):
    soma = n1 + n2 + n3
    print(soma)


soma(2, 3, 4)


# Exercício 3
def aumento(valor, percentual):
    aumento = valor + valor * (percentual/100)
    return(aumento)


print(aumento(100, 50))
print(aumento(50, 10))
print(aumento(10, 10))
print(aumento(15, 100))


# Exercício 4
def fizzbuzz(numero):
    if numero == 0:
        return numero
    elif numero % 3 == 0 and numero % 5 == 0:
        return 'FizzBuzz'
    elif numero % 3 == 0:
        return 'Fizz'
    elif numero % 5 == 0:
        return 'Buzz'
    else:
        return numero


for n in range(31):
    print(n, fizzbuzz(n))



