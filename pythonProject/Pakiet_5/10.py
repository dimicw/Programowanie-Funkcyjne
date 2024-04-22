#Stwórz generator, który produkuje nieskończony ciąg liczb Fibonacciego.
#Napisać generator, który czyta duży plik tekstowy linią po linii, unikając wczytywania całego pliku do pamięci.

def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def read_large_file(path):
    with open(path, "r") as file:
        for line in file:
            yield line.rstrip()

ffib = fib()
for _ in range(10):
    print(next(ffib))