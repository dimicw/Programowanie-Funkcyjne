#3) Zaimplementuj funkcję generatorową fibonacci, która generuje nieskończony ciąg liczb Fibonacciego i wydrukuj pierwsze 10 liczb tego ciągu.

def fibonacci():
    a, b = 0, 1

    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
first_10 = [next(fib) for _ in range(10)]
print(first_10) 