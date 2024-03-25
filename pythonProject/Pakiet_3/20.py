#20) Zdefiniuj funkcję sum_of_squares_of_odds, która oblicza sumę kwadratów liczb nieparzystych z listy.

def sum_of_squares_of_odds(numbers):
    odd = [num for num in numbers if num % 2 != 0]
    return sum(num ** 2 for num in odd)

l1 = [1,2,3,4,5,6,7,8,9]
print(sum_of_squares_of_odds(l1))