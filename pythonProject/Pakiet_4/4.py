#4) Napisz funkcję, która przyjmuje exponent i zwraca funkcję, która podnosi podaną liczbę do potęgi określonej przez ten exponent.

def f_potegowanie(exponent):
    def potegowanie(liczba):
        return liczba ** exponent
    return potegowanie

print(f_potegowanie(4)(3))