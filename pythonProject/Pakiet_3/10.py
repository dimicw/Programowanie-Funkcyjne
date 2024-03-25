#10) Zaimplementuj funkcję cumulative_sum, która oblicza sumę skumulowaną listy, tj. sumę elementów do każdego indeksu.

def cumulative_sum(lst):
    cumulative = []
    total = 0
    for n in lst:
        total += n
        cumulative.append(total)
    return cumulative

l1 = [1, 2, 3, 4]
result = cumulative_sum(l1)
print(result) 
