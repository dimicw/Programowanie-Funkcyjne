#13) Napisz funkcję split_list, która dzieli listę na podlisty o zadanej długości.

def split_list(lst, size):
    return[lst[i:i + size] for i in range(0, len(lst), size)]

l1 = [1, 2, 3, 4, 5, 6]
print(split_list(l1, 3))