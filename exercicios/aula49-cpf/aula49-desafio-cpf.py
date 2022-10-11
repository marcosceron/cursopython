"""
Desafio do CPF

CPF: 123.456.789-01 (11 dígitos)

1 - Ler um CPF no formato XXX.XXX.XXX-XX.
2 - Eliminar pontos e traço.
3 - Armazenar os 9 primeiros dígitos em uma lista (?)
4 - Percorrer a lista e multiplicar os 9 números em ordem cada um por um número
de 10 a 2 (ordem decrescente)
    X9 * 10
    X8 * 9
    etc ...
e salvar o resultado.
- Obter a soma dos resultados

5 - Calcular o seguinte:
soma1 = (11 - (soma_resultados % 11))

Se soma1 > 9:
    digito10 = 0
else:
    digito10 = soma1

6 - Armazenar o dígito

7 - Refazer o cálculo do passo 4, incluindo o dígito10
Multiplicar os 10 números em ordem por um número de 11 a 2 (ordem decrescente)

8 - Armazenar o novo cpf em uma variável
# cpf = cpf informado
# novo_cpf = cpf armazenado pelo cálculo de validação

if cpf == novo_cpf:
    valido
else:
    invalido

"""
# Ler um CPF
cpf = input('Digite um CPF: ')
tamanho_cpf = len(cpf)

# Só aceitar se o CPF tiver exatamente 14 caracteres (11 números + pontos e traço)
while tamanho_cpf != 14:
    cpf = input('Por favor, digite um CPF no formato XXX.XXX.XXX-XX: ')
    tamanho_cpf = len(cpf)

# Criar String para armazenar o valor do CPF aceitando apenas números
cpf_numerico = ''

for n in range(tamanho_cpf):
    # Checar se cada caractere da string é numérico
    # print(f'{cpf[n]} é número ' if cpf[n].isnumeric() else f'{cpf[n]} não é número')
    if cpf[n].isnumeric():
        cpf_numerico += cpf[n]

# Criar uma lista para armazenar os 9 primeiros dígitos do cpf
# int(cpf[n]): faz o cast do caractere de string para inteiro
lista_digitos = []
for n in range(len(cpf_numerico)-2):
    lista_digitos.append(int(cpf_numerico[n]))

# Percorre a lista dos 9 primeiros dígitos do CPF
# com um índice criado pela função enumerate
# dentro de um for que vai de 10 a 2, decrescente.
# Faz a primeira operação
soma_1 = 0
for indice, valor_decrescente in enumerate(range(10, 1, -1)):
    # print(lista_digitos[indice], valor_decrescente)
    multi = lista_digitos[indice] * valor_decrescente
    # print(multi)
    soma_1 += multi

# Fórmula do penúltimo dígito
# print(f'Soma 1 = {soma_1}, soma_1 % 11 = {soma_1 % 11}')
pen_dig = (11 - (soma_1 % 11))
# Se o penúltimo dígito for maior que 9 vira 0, caso contrário mantém o valor.
pen_dig = 0 if pen_dig > 9 else pen_dig

# Adiciona o penúltimo dígito no final da lista
lista_digitos.append(pen_dig)

# Percorrer novamente a lista, agora com o penúltimo dígito incluído.
# Faz a segunda operação, para o dígito final.
soma_2 = 0
for indice, valor_decrescente in enumerate(range(11, 1, -1)):
    # print(lista_digitos[indice], valor_decrescente)
    multi_2 = lista_digitos[indice] * valor_decrescente
    soma_2 += multi_2

# Fórmula do último dígito
ult_dig = (11 - (soma_2 % 11))
# Se o último dígito for maior que 9 vira 0, caso contrário mantém o valor.
ult_dig = 0 if ult_dig > 9 else ult_dig

# Adiciona o último dígito no final da lista
lista_digitos.append(ult_dig)

# String a receber o CPF a ser comparado com o que o usuário digitou
novo_cpf = ''
# Percorre a lista e adiciona cada valor na string criada
# str(lista_digitos[n]) faz o cast de int para String a cada iteração
for n in range(len(lista_digitos)):
    novo_cpf += str(lista_digitos[n])

# print(f'CPF do usuário: {cpf_numerico} | CPF a validar: {novo_cpf}')

# Evita sequencias. Ex.: 11111111111, 00000000000...
sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf_numerico)


# Mensagem final
print(f'O CPF {cpf} é válido!') if cpf_numerico == novo_cpf and not sequencia else print(f'O CPF {cpf} é **INVÁLIDO**!')
