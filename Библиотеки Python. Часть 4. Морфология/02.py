import sys
import pymorphy2
morph = pymorphy2.MorphAnalyzer()
a = sys.stdin.read().lower().replace("-", " ")
e = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя \n"
b = "".join([i for i in a if i in e]).split()
c = list(filter(lambda x: morph.parse(x)[0].score > 0.5 and morph.parse(x)[0].tag.POS == 'NOUN', b))
c = list(map(lambda x: morph.parse(x)[0].normal_form, c))
print(*sorted(set(c), key=lambda x: (c.count(x), x), reverse=True)[:10])
