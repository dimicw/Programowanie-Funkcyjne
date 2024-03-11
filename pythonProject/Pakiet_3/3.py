def recrsive_sum(nested_list):
    total = 0

    for item in nested_list:
        if isinstance(item, int):
            total += item
        elif isinstance(item, list):
            total += recrsive_sum(item)
    
    return total

l1 = [[[1, 2, 3], 4, [5, 6]], 7, [8, 9], 0]
print(recrsive_sum(l1))