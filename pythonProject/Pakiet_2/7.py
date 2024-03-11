#7) Użyj funkcji groupby z modułu itertools, aby zgrupować ciąg liczb całkowitych na podstawie ich parzystości i wydrukować wynikowe grupy.

from itertools import groupby

def is_even(n):
    return n % 2 == 0

l1 = [0,1,2,3,4,5,6,7,8,9]
l2 = {k: list(v) for k, v in groupby(l1, key = is_even)}

print(l2)