n = int(input())
war = "Евразия"
peace = "Остазия"
for _ in range(n):
    command = input()
    if command == "С кем война?":
        print(war)
    elif command == "С кем мир?":
        print(peace)
    elif command == "Меняем":
        war, peace = peace, war
