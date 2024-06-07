d = {}
for _ in range(int(input())):
    x = input()
    word = x.split()
    d[word[0]] = x[len(word[0]) + 1:]

for _ in range(int(input())):
    word = input()
    if word not in d:
        print('Нет в словаре')
    else:
        print(d[word])
