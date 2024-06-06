seconds_left = int(input())
if seconds_left >= 0:
    for i in range(seconds_left, -1, -1):
        print(f"Осталось секунд: {i}")
    print("Пуск")
else:
    print("Пуск")
