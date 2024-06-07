words = set()

while True:
    word = input()
    if word == "стоп":
        break
    words.add(word)

if len(words) < 2:
    print("НЕТ")
else:
    shortest = min(words, key=len)
    longest = max(words, key=len)

    has_all_letters = True
    for letter in shortest:
        if letter not in longest:
            has_all_letters = False
            break

    print("ДА" if has_all_letters else "НЕТ")
