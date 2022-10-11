"""
+, -, *, /, //, **, %, ()
"""
print(5 * 'Str ')
print(5 * 3)
print('5' + ' - Str')

print(2 + 5 * 3 ** 2 - (23.5 +23.5))
# print(2+5*9-(47))
# print(2+45-(47))
# resultado = 0

def verificaNumeroPrimo(numero):
    count = 0;
    for n in range(1, numero + 1):
        if (numero % n == 0):
            count += 1
    if count == 2:
        print("O número " + str(numero) + " é primo")
    # else:
    # print("O número " + str(numero) + " não é primo")


for n in range(1, 100):
    verificaNumeroPrimo(int(n))
