import random
import math
list_s = [round(random.uniform(1, 100) ,2) for item in range(15)]
print(list_s)
for item in list_s:
    drob_ch = math.floor((item*100)%100)  #здесь вычисляю дробную часть числа
    if len(str(drob_ch)) == 1:            # здесь добавляю 0 перед копейками где надо
        drob_ch = '0' + str(item).split('0')[-1]
    print(round(item // 1), 'руб.',   drob_ch, 'коп.')
