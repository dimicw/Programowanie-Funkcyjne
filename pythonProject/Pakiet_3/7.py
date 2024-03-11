#7) Napisz funkcję flatten_list, która spłaszcza zagnieżdżone listy do pojedynczej listy.

def flatten_list(nested_list):
    flattened = []
    for item in nested_list:
        if isinstance(item, list):
            flattened.extend(flatten_list(item))
        else:
            flattened.append(item)
    return flattened

l1 = [1, [2, 3, [4, 5, 6]], 7, [8, 9], 0]

print(flatten_list(l1))