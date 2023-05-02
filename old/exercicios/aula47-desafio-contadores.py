c = 10
for n in range(9):
    print(n, c)
    c -= 1

print('####')

# Solução do professor:
for p, r in enumerate(range(10, 1, -1)):
    print(p, r)