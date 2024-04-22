#Korzystając z funkcji filter(), wyodrębnić z danej listy słów te, które zaczynają się na literę 'a'.
#Użyj funkcji map() do przekształcenia listy liczb w listę ich kwadratów.

def filter_a(words):
    return(list(filter(lambda x: x.startswith('a'), words)))

def squares(numbers):
    return list(map(lambda x: x ** 2, numbers))

print(filter_a(["aaa", "asd", "asdf", "Aqwe", "qwe", "zcx"]))
print(squares([1,2,3,4,5]))