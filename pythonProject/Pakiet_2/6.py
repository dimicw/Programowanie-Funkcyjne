#6) Zaimplementuj dekorator safe_function, który łapie wyjątki podczas wywołania funkcji i zamiast przerywać program, wypisuje informację o błędzie i zwraca None. 
#Przetestuj dekorator na funkcji dzielącej dwie liczby.

def safe(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as ex:
            print(f"Error: {ex}")
            return None
    return wrapper


@safe
def divide(a, b):
    return a/b


print(divide(0, 0))
print(divide(0, 4))
print(divide(4, 0))
print(divide(4, 4))