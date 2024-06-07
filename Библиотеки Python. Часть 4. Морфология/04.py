import pymorphy3

morph = pymorphy3.MorphAnalyzer()
text = morph.parse(input())[0]

CAse = ['Именительный падеж:', 'Родительный падеж:', 'Дательный падеж:', 'Винительный падеж:', 'Творительный падеж:',
        'Предложный падеж:']
Case = ['nomn', 'gent', 'datv', 'accs', 'ablt', 'loct']

if 'NOUN' not in text.tag:
    print('Не существительное')

else:
    print('Единственное число:')

for i in range(7 - 1):
    print(CAse[i], text.inflect({'sing', Case[i]})[0])
    print('Множественное число:')

for i in range(7 - 1):
    print(CAse[i], text.inflect({'plur', Case[i]})[0])
