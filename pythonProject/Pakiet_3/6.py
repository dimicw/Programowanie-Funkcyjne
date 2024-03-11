def map_nested(func, nested_list):
    if isinstance(nested_list, list):
        return [map_nested(func, item) for item in nested_list]
    else:
        return func(nested_list)

l1 = [1, [2, 3, [4, 5, 6]], 7, [8, 9], 0]

print(map_nested(lambda x: x * 10, l1))