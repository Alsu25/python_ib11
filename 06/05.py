english, german, french = map(int, input().split())
names = []
for _ in range(english + german + french):
    names.append(input())

english_set = set(names[:english])
german_set = set(names[english:english + german])
french_set = set(names[english + german:])

count = 0
for name in names:
    if len({name} & english_set & german_set) == 2:
        count += 1
    elif len({name} & english_set & french_set) == 2:
        count += 1
    elif len({name} & german_set & french_set) == 2:
        count += 1

if count == 0:
    print("NO")
else:
    print(count)
