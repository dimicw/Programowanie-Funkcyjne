#18) Zaimplementuj funkcję transpose_matrix, która transponuje macierz (zamienia wiersze na kolumny i odwrotnie).

def transpose_matrix(matrix):
    return[list(row) for row in zip(*matrix)]

m = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8 ,9]
]

print(transpose_matrix(m))