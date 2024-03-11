def generate_infinite_sequence():
    n = 0
    while True:
        yield n
        n += 2

        
generator = generate_infinite_sequence()

print(next(generator))
print(next(generator))
