#10) Napisz funkcję, która generuje wszystkie permutacje elementów listy.

from itertools import permutations

def permutacje(lista):
    return list(permutations(lista))

l1 = [1, 2, 3, 4]
print(permutacje(l1))