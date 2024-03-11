#4) Użyj wyrażenia walrus operator (:=) wewnątrz list comprehension, aby stworzyć i wydrukować listę kwadratów liczb z podanej listy, które są większe niż 10.

liczby = [1,2,3,4,5,6,7,15,28,123]
over_10 = [x*x for x in liczby if x > 10]

print(over_10)