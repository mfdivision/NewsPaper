import re

bad_words = ['Дурак', 'Редиска', 'Обормот']
text = 'Высокий дурак уровень вовлечения обормот представителей целевой аудитории является четким'

text_f = text.split()
for i in text_f:

    if i in bad_words or i.capitalize() in bad_words:
        l = len(i)-1
        i_new = i.replace(i, f'''{i[0]}{('*' * l)}''')

        print(i_new)

        text = text.replace(i, i_new)

print(text)