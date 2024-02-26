import time


def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"czas: {end - start}")
        return result

    return wrapper


@timeit
def f1(x):
    time.sleep(1)
    return x + 123


f1(10)
