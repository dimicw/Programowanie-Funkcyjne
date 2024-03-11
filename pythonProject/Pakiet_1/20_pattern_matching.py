#20) Napisz funkcję, która używa dopasowania wzorców do analizy i reakcji na różne struktury danych (np. listy, krotki).

def pattern_matching(data):
    match data:
        case (x, y):
            return f"Tupla: {x}, {y}"
        case [x, y, z]:
            return f"Lista: {x}, {y}, {z}"
        case _: 
            return "nie rozpoznano"