#5) Napisz jednolinijkową funkcję is_palindrome, która sprawdza, czy dany ciąg znaków (bez uwzględniania wielkości liter i białych znaków) jest palindromem.

is_palindrome = lambda s: s.lower().replace(" ", "") == s[::-1].lower().replace(" ", "")

print(is_palindrome("Kamil Ślimak"))
print(is_palindrome("Adam Ślimak"))