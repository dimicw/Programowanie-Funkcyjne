#Napisać funkcję, która przyjmuje listę liczb i zwraca listę zawierającą tylko te liczby, które są parzyste.
#Użyj wyrażenia lambda do stworzenia funkcji, która oblicza pole prostokąta na podstawie długości jego boków.

def even(numbers):
    return list(filter(lambda x: x % 2 == 0, numbers))

area = lambda length, width: length * width

print(even([1,2,3,4,5,6,7,8,99]))
print(area(2,3))