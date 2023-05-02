nome = input('Digite o primeiro nome: ')
comp = len(nome)

if comp <= 4:
    print("Seu nome é curto.")
elif comp > 4 and comp <= 6:
    print("Seu nome é normal.")
else:
    print("Seu nome é muito grande.")