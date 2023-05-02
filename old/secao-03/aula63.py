print()
print('Texto explicativo.')

perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2? ',
        'respostas': {'a': '1', 'b': '4', 'c': '5',},
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 3*2? ',
        'respostas': {'a': '4', 'b': '10', 'c': '6', },
        'resposta_certa': 'c',
    },
    'Pergunta 3': {
        'pergunta': 'Quanto é 1+2? ',
        'respostas': {'a': '4', 'b': '3', 'c': '6', },
        'resposta_certa': 'b',
    },
    'Pergunta 4': {
        'pergunta': 'Quanto é 1-1? ',
        'respostas': {'a': '0', 'b': '100', 'c': '1.5', },
        'resposta_certa': 'a',
    },
    'Pergunta 5': {
        'pergunta': 'Quem fundou o SBT? ',
        'respostas': {'a': 'Cabral', 'b': 'Napoleão', 'c': 'Silvio Santos', },
        'resposta_certa': 'c',
    },
}
print()

respostas_certas = 0

for pk, pv in perguntas.items():
    print(f"{pk}: {pv['pergunta']}")

    print('Opções: ')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    resposta_usuario = input('Sua resposta: ')
    while len(resposta_usuario) != 1 or not resposta_usuario.isalpha():
        resposta_usuario = input('Resposta inválida! Tente novamente: ')

    if resposta_usuario == pv['resposta_certa']:
        print('Você acertou!')
        respostas_certas += 1
    else:
        print('Você errou!')

    print()

qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perguntas * 100


if respostas_certas == 0:
    print(f'Você não acertou nenhuma pergunta.')
elif respostas_certas == 1:
    print(f'Você acertou uma pergunta.')
else:
    print(f'Você acertou {respostas_certas} perguntas.')

print(f'Sua porcentagem de acerto foi de {porcentagem_acerto}%.')