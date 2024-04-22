#Użyj funkcji reduce() z modułu functools, aby znaleźć największą liczbę w liście.
#Napisać funkcję używając reduce(), która oblicza średnią z listy liczb.

from functools import reduce

def max(l1):
    return reduce(lambda a, b: a if a > b else b, l1)

def avg(l1):
    return reduce(lambda a, b: a + b, l1) / len(l1)

print(max([1,2,3,4,5,6,99,88]))
print(avg([1,3,20,33,1]))