translated_text = ''


def translate(text):
    global translated_text
    a = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е',
         'А', 'У', 'О', 'Ы', 'И', 'Э', 'Я', 'Ю', 'Ё', 'Е',
         '.', ',', '-']
    if len(text) == 0:
        return ''
    else:
        text = list(map(str, text))
        for i in text:
            if i in a:
                text.remove(i)
        for j in text:
            if j in a:
                text.remove(j)
        translated_text = ''.join(text)
        translated_text = translated_text.split()
        translated_text = ' '.join(translated_text)