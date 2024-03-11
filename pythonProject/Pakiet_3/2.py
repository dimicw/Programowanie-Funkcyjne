def filter_long_words(words):
    avg_len = sum(len(word) for word in words) / len(words)
    return [word for word in words if len(word) > avg_len]

l1 = ["Adam", "Bartłomiej", "Celina", "Dominik", "Elżbieta"]

print(filter_long_words(l1))