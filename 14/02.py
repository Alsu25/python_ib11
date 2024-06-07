def space_game(text):
    c = 0
    for i in text:
        if i == " ":
            c += 1
    if c % 2 == 0:
        print("Вы выиграли")
    else:
        print("Вы проиграли")


s = input("Введите текст: ")

space_game(s)
