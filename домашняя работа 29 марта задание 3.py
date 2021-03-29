

def thesaurus(*names):
    lst = {}
    for item in names:
        key = item[0].capitalize()
        if key not in lst:
            lst[key] = []
        lst[key].append(item)
    return lst

print(thesaurus("Иван", "Мария", "Петр", "Илья"))