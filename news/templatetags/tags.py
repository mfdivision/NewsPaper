from datetime import datetime

from django import template


register = template.Library()


@register.simple_tag()
def current_time(format_string='%b %d %Y'):
    return datetime.utcnow().strftime(format_string)


@register.filter()
def censor(text):
    bad_words = ['Дурак', 'Редиска', 'Обормот']

    for i in text.split():
        l = len(i) - 1
        if i in bad_words or i.capitalize() in bad_words:
            i_new = i.replace(i, f'''{i[0]}{('*' * l)}''')
            text = text.replace(i, i_new)
        elif i.lower in bad_words:
            i_new = i.replace(i, f'''{i[0]}{('*' * l)}''')
            text = text.replace(i, i_new)

    return text
