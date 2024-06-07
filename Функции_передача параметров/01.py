def parrot(phrase):
    if phrase in list_words:
        print(phrase)
    else:
        list_words.append(phrase)


parrot("Привет")
parrot("Как тебя зовут?")
parrot("Привет")