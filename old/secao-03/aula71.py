import sys
import time

#
# def gera():
#     # for n in range(100):
#     #     yield n
#     #     time.sleep(0.1)
#     variavel = 'Valor 1'
#     yield variavel
#     variavel = 'Valor 2'
#     yield variavel
#     variavel = 'Valor 3'
#     yield variavel
#
# g = gera()
#
# for v in g:
#     print(v)


# lista = list(range(1000))
l1 = [x for x in range(100)]

l2 = (x for x in range(100))

print(next(l2))
print(next(l2))
print(next(l2))
print(next(l2))

for v in l2:
    print(v)
