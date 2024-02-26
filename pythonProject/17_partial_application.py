from functools import partial


def add(x, y):
    return x + y


add_five = partial(add, 5)
print(add_five(10))
