#Napisać dwie funkcje: jedna, która podnosi liczbę do kwadratu, a druga, która dodaje do liczby 5.
#Stwórz funkcję, która łączy funkcje, aby zastosować obie funkcje do listy liczb.
#Następnie aplikuj wszystkie funkcje do tej wartości.

def square(x): 
    return x **2

def add5(x):
    return x + 5

def apply_all(funcs, values):
    return [[f(v) for f in funcs] for v in values]

print(apply_all([square, add5], [1,2,3,4]))