#1) Użyj funkcji product z modułu itertools, aby wygenerować i wydrukować wszystkie możliwe kombinacje liter z dwóch list: ['A', 'B'] i ['C', 'D'].

from itertools import product

l1 = ['A', 'B']
l2 = ['C', 'D']
combinations = list(product(l1, l2))

print(combinations)