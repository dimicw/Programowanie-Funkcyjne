#16) Zdefiniuj funkcję remove_whitespace, która usuwa białe znaki z każdego elementu listy stringów.

def remove_whitespace(lst):
    return[s.replace(" ", "") for s in lst]

l1 = ["a a", "bb", " c    c   c c cc", "     "]
print(remove_whitespace(l1))