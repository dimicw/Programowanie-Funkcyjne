#5) Napisz funkcję, która dzieli listę na części o określonej maksymalnej długości.

def podziel(lista, dlugosc):
    return [lista[i : i + dlugosc] for i in range(0, len(lista), dlugosc)]

l1 = [1,2,3,4,5,6,7,8,9,0]
print(podziel(l1, 3))