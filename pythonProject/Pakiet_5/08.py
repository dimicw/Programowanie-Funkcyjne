#Stwórz listę zawierającą pierwsze 10 liczb kwadratowych (1, 4, 9, ...) używając list comprehensions.
#Użyj list comprehensions, aby z danej listy słów stworzyć listę długości tych słów.

squares = [x ** 2 for x in range(1,11)]
lenghts = [len(word) for word in ["asd", "qwerty", "lk", "poiuyytr"]]

print(squares)
print(lenghts)