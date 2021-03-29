list_s = ['в', '"05"', 'часов', '"17"', 'минут', 'температура', 'воздуха', 'была', '"+05"', 'градусов']
message = ''
for item in list_s:
    message += item
    message += ' '
print(message)
