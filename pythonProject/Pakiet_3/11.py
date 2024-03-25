#11) Napisz funkcję find_max_min_diff, która znajduje różnicę między maksymalną a minimalną wartością w liście.

def find_max_min_diff(lst):
    return max(lst) - min(lst)

l1 = [1, 2, 3, 4, 5, 6]
print(find_max_min_diff(l1))