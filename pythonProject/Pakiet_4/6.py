#6) Napisz funkcję, która przyjmuje listę i funkcję, a następnie zwraca nową listę, gdzie każdy element jest wynikiem zastosowania funkcji do dotychczasowych elementów.

def zastosuj(lista, funkcja):
    return [funkcja(x) for x in lista]

l1 = [0, 1, 2, 3, 4, 10]
def f1(x):
    return x * x
print(zastosuj(l1, f1))