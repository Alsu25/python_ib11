message = input()
number = int(input())

if 1 <= number <= len(message):
  print(message[number - 1])
else:
  print("ОШИБКА")

