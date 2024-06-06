number = float(input("Введите дробное число: "))
if abs(number) < 1e-6:
    print("Миллион")
else:
    print(1 / number)
