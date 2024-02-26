def generate_infinite_sequence():
    num = 0
    while True:
        yield num
        num += 2

        
generator = generate_infinite_sequence()

print(next(generator))
print(next(generator))
