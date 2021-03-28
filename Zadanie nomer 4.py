list_s = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
mess = ' '.join(list_s)
name_igor_correct = mess[mess.index('И'):mess.index(' гл')]

name_marina_correct = mess[mess.index('М'):mess.index(' ток')].lower()

name_nikolai_correct = mess[mess.index('нИ'):mess.index(' ди')].lower()

name_ailita_correct = mess[mess.index('аэ'):]

# исправляю имена
name_nikolai_correct = (chr(ord(name_nikolai_correct[0]) - 32) + name_nikolai_correct[1:])
name_marina_correct = (chr(ord(name_marina_correct[0])-32) + name_marina_correct[1:])
name_ailita_correct = (chr(ord(name_ailita_correct[0])-32) + name_ailita_correct[1:])

print('Привет,', name_igor_correct + '!')
print('Привет,', name_marina_correct + '!')
print('Привет,', name_nikolai_correct + '!')
print('Привет,', name_ailita_correct + '!')



