import pymorphy2

i = 99
w = pymorphy2.MorphAnalyzer().parse('бутылка')[0]

while i:
    print('В холодильнике', i, w.make_agree_with_number(i).word, 'кваса.\nВозьмём одну и выпьем.')
    i -= 1
    if i % 10 == 1 and i != 11:
        o = 'Осталась'
    else:
        o = 'Осталось'
    print(o, i, w.make_agree_with_number(i).word, 'кваса.')