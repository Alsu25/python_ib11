n = int(input())
phonebook = {}
for _ in range(n):
    phone, name = input().split()
    if name not in phonebook:
        phonebook[name] = []
    phonebook[name].append(phone)

m = int(input())
for _ in range(m):
    name = input()
    if name in phonebook:
        print(' '.join(phonebook[name]))
    else:
        print('Нет в телефонной книге')
