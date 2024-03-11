#9) Stwórz i wydrukuj macierz 3x3 za pomocą zagnieżdżonej listy składanej, wypełnioną wartościami od 1 do 9.

matrix = [[(i * 3) + j + 1 for j in range(3)] for i in range(3)]

print(matrix)