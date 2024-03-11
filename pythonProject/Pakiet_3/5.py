def generate_fibonacci():
    a, b = 0, 1

    while True:
        yield a
        a, b = b, a + b

fib = generate_fibonacci()
first_10 = [next(fib) for _ in range(10)]
print(first_10) 