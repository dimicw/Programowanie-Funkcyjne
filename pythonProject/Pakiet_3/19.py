#19) Napisz funkcję check_anagrams, która sprawdza, czy dwa podane stringi są anagramami.

def check_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

s1 = "qwerty"
s2 = "ewqryt"
s3 = "aaaaaa"

print(check_anagrams(s1, s2))
print(check_anagrams(s1, s3))