def add(x):
    def inner(y):
        return x + y
    return inner


add_five = add(5)
print(add_five(10))