# add (adiciona), update (atualiza), clear, discard
# union | (une)
# intersection & (todos os elementos presentes nos dois sets)
# difference - (elementos apenas no set da esquerda)
# symmetric_difference ^ (elementos que estão nos dois sets, mas não em ambos)

# s1 = {1,2,3,4,5}
#
# for v in s1:
#     print(v)

s1 = set()
# s1.add(1)
# s1.add(2)
# s1.add((1,2,3,'Fulano'))
#
# s1.discard(2)

# s1.update('Python')

# s1.update([1,2,3,4,5], {5,6,7,8})
#
# print(s1)


# l1 = [1,2,1,1,3,4,5,6,6,6,6,6,6,7,8,9, 'Ana', 'Ana']
# l1 = set(l1)
# l1 = list(l1)
#
#
# print(l1)
# print(l1[-1])

# s1 = {1, 2, 3, 4, 5}
# s11 = {1, 2, 3, 4, 5, 7}
# s2 = {1, 2, 3, 4, 5, 6}
#
#
# # Union
# s3 = s1 | s2
# s3_2 = s1.union(s2)
#
# # Intersection
# s4 = s1 & s2
#
# # Difference
# s5 = s11 - s2
#
# # Symmetric Difference
# s6 = s2 ^ s11
# s7 = s2.symmetric_difference(s11)
#
#
# print(s3)
# print(s3_2)
# print(s4)
# print(s5)
# print(s6)
# print(s7)

l1 = ['Ramon', 'Frederico', 'Zenon']
l2 = ['Frederico', 'Zenon', 'Zenon', 'Ramon', 'Ramon', 'Ramon']

# l1 = list(set(l1))
# l2 = list(set(l2))
#
# print(l1, l2)

if set(l1) == set(l2):
    print('L1 é igual a L2')
else:
    print('L1 é diferente de L2')