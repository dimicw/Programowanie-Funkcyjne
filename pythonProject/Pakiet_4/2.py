#2) Napisz funkcję, która przyjmuje string i zwraca nowy string, w którym wszystkie wielkie litery są zamienione na małe, a małe na wielkie.

def swap(text):
    return text.swapcase()

s1 = "AaBb Cc"
print(swap(s1))