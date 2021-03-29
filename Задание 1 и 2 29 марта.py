

def num_translate(word):

    if word == 'one' or word == 'One':
        if word == 'one':
            word = 'один'
        else:
            word = 'Один'

    elif word == 'two'or word == 'Two':
        if word == 'two':
            word = 'два'
        else:
            word = 'Два'

    elif word == 'three' or word == 'Three':
        if word == 'three':
            word = 'три'
        else:
            word = 'Три'

    elif word == 'four' or word == 'Four':
        if word == 'four':
            word = 'четыре'
        else:
            word = 'Четыре'

    elif word == 'five' or word == 'Five':
        if word == 'five':
            word = 'пять'
        else:
            word = 'Пять'

    elif word == 'six' or word == 'Six':
        if word == 'six':
            word = 'шесть'
        else:
            word = 'Шесть'

    elif word == 'seven' or word == 'Seven':
        if word == 'seven':
            word = 'семь'
        else:
            word = 'Семь'

    elif word == 'eight' or word == 'Eight':
        if word == 'eight':
            word = 'восемь'
        else:
            word = 'Восемь'

    elif word == 'nine' or word  == 'Nine':
        if word == 'nine':
            word = 'девять'
        else:
            word = 'Девять'

    elif word == 'ten' or word == 'Ten':
        if word == 'ten':
            word = 'десять'
        else:
            word = 'Десять'

    else: return None
    return word


print(num_translate('one'))
print(num_translate('One'))

print('')

print(num_translate('two'))
print(num_translate('Two'))

print('')

print(num_translate('three'))
print(num_translate('Three'))

print('')

print(num_translate('four'))
print(num_translate('Four'))

print('')

print(num_translate('five'))
print(num_translate('Five'))

print('')

print(num_translate('six'))
print(num_translate('Six'))

print('')

print(num_translate('seven'))
print(num_translate('Seven'))

print('')

print(num_translate('eight'))
print(num_translate('Eight'))

print('')

print(num_translate('nine'))
print(num_translate('Nine'))

print('')

print(num_translate('ten'))
print(num_translate('Ten'))