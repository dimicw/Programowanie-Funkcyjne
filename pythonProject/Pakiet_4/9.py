#9) Napisz funkcję, która przyjmuje listę krotek i zwraca listę, w której każdy element jest wynikiem zastosowania funkcji do elementów krotek.

def funkcja_do_krotek(lista, funkcja):
    return [funkcja(*krotka) for krotka in lista]

l1 = []
def f1(x, y):
    return x + y

l1 = [(1, 2), (3, 4), (5, 6), (1, 1)]
print(funkcja_do_krotek(l1, f1))