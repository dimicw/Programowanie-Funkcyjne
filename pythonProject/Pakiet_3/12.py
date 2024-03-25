#12) Zdefiniuj funkcję rotate_list, która obraca listę o zadaną liczbę kroków w prawo.

def rotate_list(lst, n):
    n %= len(lst)
    return lst[-n:] + lst[:-n]

l1 = [1, 2, 3, 4, 5, 6]
print(rotate_list(l1, 2))