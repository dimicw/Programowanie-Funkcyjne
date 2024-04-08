#8) Napisz funkcję, która zwraca najczęściej występujący element w liście. W przypadku remisu zwróć jeden z nich.

def najczestszy(lista):
    return max(set(lista), key = lista.count)

l1 = [1, 1, 3, 2, 2, 2, 23]
print(najczestszy(l1))