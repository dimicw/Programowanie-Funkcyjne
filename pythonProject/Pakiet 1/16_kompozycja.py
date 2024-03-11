def add_five(x):
    return x + 5


def multiply_by_two(x):
    return x * 2


def compose(f, g):
    return lambda x: f(g(x))


add_then_multiply = compose(multiply_by_two, add_five)
print(add_then_multiply(10))
