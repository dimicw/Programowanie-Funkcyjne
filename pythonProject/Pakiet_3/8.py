#8) Zdefiniuj funkcję partition_list, która dzieli listę na dwie części: jedną zawierającą elementy spełniające warunek, a drugą zawierającą pozostałe elementy.


def partition_list(lst, condition):
    true_list = [item for item in lst if condition(item)]
    false_list = [item for item in lst if not condition(item)]
    return true_list, false_list


numbers = [1, 2, 3, 4, 5, 6]
even, odd = partition_list(numbers, lambda x: x % 2 == 0)
print(even)
print(odd)