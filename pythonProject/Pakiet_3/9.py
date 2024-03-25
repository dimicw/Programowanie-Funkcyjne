#9) Napisz funkcję zip_with_index, która łączy elementy listy z ich indeksami.

def zip_with_index(lst):
    return list(enumerate(lst))

l1 = ["a", "b", "c", "d"]
print(zip_with_index(l1))