#15) Napisz funkcję custom_sort, która sortuje listę według zadanej funkcji klucza.

def custom_sort(lst, k):
    return sorted(lst, key = k)

l1 = ["q", "W", "e", "Rty"]
print(custom_sort(l1, lambda x: x.lower()))