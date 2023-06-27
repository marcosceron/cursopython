"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""
while True:
    cpf = input("Digite um CPF [xxx.xxx.xxx-xx]: ")
    # Validação
    while len(cpf) != 14:
        print("CPF inválido")
        cpf = input("Digite um CPF:")
    
    cpf_num = cpf.replace('.', '').replace('-', '')
    cpf_input_e_sequencial = cpf_num == cpf_num[0] * len(cpf_num)
    
    if cpf_input_e_sequencial: print(f'{cpf} é um número sequencial')

    multiplicador = 10
    soma = 0
    nove_digitos = cpf_num[:9]

    for i in range(9):
        n_cpf = int(nove_digitos[i])
        valor_atual = n_cpf * multiplicador
        # print(f'{n_cpf} x {multiplicador} = {valor_atual}')
        soma += valor_atual
        multiplicador -= 1

    # print(soma)
    dv_1 = (soma * 10) % 11
    # Verificar se é maior que 9
    dv_1 = dv_1 if dv_1 <= 9 else 0

    # Segundo DV
    multiplicador = 11
    soma = 0
    dez_digitos = nove_digitos + str(dv_1)
    for i in range(10):
        n_cpf = int(dez_digitos[i])
        valor_atual = n_cpf * multiplicador
        # print(f'{n_cpf} x {multiplicador} = {valor_atual}')
        soma += valor_atual
        multiplicador -= 1
    
    # print(soma)
    dv_2 = (soma * 10) % 11
    # Verificar se é maior que 9
    dv_2 = dv_2 if dv_2 <= 9 else 0
    # print(n_resultante)
    cpf_calculado = f'{nove_digitos}{dv_1}{dv_2}'
    
    if cpf_num == cpf_calculado and not cpf_input_e_sequencial:
        print(f'O CPF {cpf} é válido!')
    else:
        print(f'O CPF {cpf} é INVÁLIDO!')