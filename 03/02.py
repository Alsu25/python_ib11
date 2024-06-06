password1 = input()
password2 = input()
if password1 != password2:
    print('Различаются.')
elif len(password1 or password2) < 8:
    print('Короткий!')
else:
    print("ОК")