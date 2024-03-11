def remove_duplicates(input_list):
    unique = []
    for item in input_list:
        if item not in unique:
            unique.append(item)

    return unique

l1 = ["Adam", "Bożena", "Adam", "Kasia", "Dominik", "Kasia", "Adam"]

print(remove_duplicates(l1))