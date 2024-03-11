#2) Napisz funkcję, która przyjmuje listę elementów i zwraca listę wszystkich możliwych 2-elementowych kombinacji tych elementów.

from itertools import combinations
def all_combinations(elements):
    return list(combinations(elements, 2))

l1 = [1,2,3,4,5,6]
print(all_combinations(l1))