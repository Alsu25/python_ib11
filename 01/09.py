username = input()
address = input()
if '@' not in username and '@' in address:
    print("ОК")
elif "@" in username and "@" in address:
    print('Некорректный логин')
elif "@" not in username and "@" not in address:
    print("Некорректный адрес")

