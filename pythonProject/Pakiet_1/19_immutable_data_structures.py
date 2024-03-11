#19) Pokaż przykład funkcji, która operuje na niemutowalnych strukturach danych, takich jak krotki (tuple).


def update_tuple(oryginal, value, index):
        temp_list = list(oryginal)
        temp_list[index] = value
        return tuple(temp_list)

t1 = (1, 3, 5)
t2 = update_tuple(t1, 2, 2)

print(t1)
print(t2)