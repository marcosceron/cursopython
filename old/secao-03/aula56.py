# def func(a1, a2, a3, nome=None, a4=None):
#     print(a1, a2, a3, nome, a4)
#     return nome, a4
#
#
# func(1,2,3, nome='Luiz', a4=4)
# var = func(1,2,3, 'Fulano', 7)
#
# print(var[0], var[1])

def func(*args, **kwargs):
    print(args)

    idade = kwargs['idade']
    print(idade)



lista = [1,2,3,4,5]
lista2 = [10, 20, 30, 40, 50]
func(*lista, *lista2, nome='Luiz', sobrenome='Miranda', idade=30)