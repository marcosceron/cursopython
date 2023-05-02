from random import randint

for i in range(10000):
    num = randint(000, 999)
    num = str(num).zfill(3)
    if num[0] == '0':
        print(f'O número {num} começa com 0.')
        break
