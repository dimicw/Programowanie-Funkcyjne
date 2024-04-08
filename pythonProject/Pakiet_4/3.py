#3) Napisz funkcję, która przyjmuje słownik i filtruje go, pozostawiając tylko te elementy, których wartości są liczbami parzystymi.

def parzyste(slownik):
    return {k: v for k, v in slownik.items() if isinstance(v, int) and v % 2 == 0}

d1 = {
    1: 'a',
    2: 4,
    3: 'c',
    4: 11,
    5: 15,
    6: 'f',
    7: 22
}
d2 = parzyste(d1)
print(d2.get(2))
print(d2.get(3))
print(d2.get(4))