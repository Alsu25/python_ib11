def print_document(pages):
    s = []
    for i in pages:
        if 'Секретно' in i:
            break
        else:
            s.append(i)
    for j in s:
        print(j, end='\n')
    if s == pages:
        print('Напечатано без купюр')
    else:
        print('Дальнейшие материалы засекречены')
