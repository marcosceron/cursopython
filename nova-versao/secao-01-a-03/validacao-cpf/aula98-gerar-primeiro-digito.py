"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

while True:
    cpf = input("Digite um CPF:")

    while len(cpf) != 11 or not cpf.isnumeric():
        print("CPF inválido")
        cpf = input("Digite um CPF:")


    # Percorrer os 9 primeiros números
    # Preciso de um multiplcador de 10 a 2
    # e de uma soma total
    multiplicador = 10
    soma = 0

    for i in range(9):
        n_cpf = int(cpf[i])
        valor_atual = n_cpf * multiplicador
        # print(f'{n_cpf} x {multiplicador} = {valor_atual}')
        soma += valor_atual
        multiplicador -= 1

    # print(soma)
    # Multiplicar o resultado da expressão por 10
    # Obter o resto da divisão da conta anterior por 11
    n_resultante = (soma * 10) % 11

    # Verificar se é maior que 9
    n_resultante = n_resultante if n_resultante <= 9 else 0
    print(n_resultante)
