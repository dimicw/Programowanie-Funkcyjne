#14) Zaimplementuj funkcję count_unique_elements, która zlicza unikalne elementy w liście.

def count_unique_elements(lst):
    return len(set(lst))

l1 = [1, 2, 3, 4, 5, 6, 6, 6, 6, 3, 6, 2, 9, 6, 6, 1]
print(count_unique_elements(l1))