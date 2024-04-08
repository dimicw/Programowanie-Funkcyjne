#1) Napisz funkcję, która przyjmuje listę liczb całkowitych i zwraca sumę wszystkich parzystych liczb w tej liście.

def sum_even(listOfNumbers):
    return sum(x for x in listOfNumbers if x % 2 == 0)

l1 = [1, 2, 3, 4, 5, 6]
print(sum_even(l1))