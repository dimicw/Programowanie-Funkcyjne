#10) Napisz funkcję concat_strings, która przyjmuje nieokreśloną liczbę argumentów typu string i łączy je w jeden ciąg znaków, rozdzielając spacją. Przetestuj funkcję na kilku zestawach stringów.

def concat_strings(*args):
    return ' '.join(args)

print(concat_strings("Test", "test", ":)"))