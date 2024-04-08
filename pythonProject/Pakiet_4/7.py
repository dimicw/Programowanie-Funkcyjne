#7) Napisz funkcję, która łączy dowolną liczbę słowników w jeden słownik, gdzie wartości dla powtarzających się kluczy są sumowane.

def polacz_slowniki(*slowniki):
    wynik = {}
    for slownik in slowniki:
        for k, v in slownik.items():
            wynik[k] = wynik.get(k, '') + v
    return wynik

d1 = {
    1: 'a',
    2: 'b',
    3: 'c'
}
d2 = {
    4: 'd',
    5: 'e',
    6: 'f',
    7: 'g',
    2: 'z'
}
d3 = {11: "abc"}
d4 = polacz_slowniki(d1, d2, d3)
print(d4.get(1))
print(d4.get(2))
print(d4.get(5))
print(d4.get(11))
print(d4.get(12))
