#17) Napisz funkcję capitalize_all_words, która zamienia pierwszą literę każdego słowa w stringu na wielką literę.

def capitalize_all_words(str):
    return ' '.join(word.capitalize() for word in str.split())

s = "aa bbbbbb cccccccccc d eee"
print(capitalize_all_words(s))