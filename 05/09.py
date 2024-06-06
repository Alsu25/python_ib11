num_lines = int(input())
cat_found = False
dog_found = False

for i in range(num_lines):
    line = input()
    if "Кот" in line or "кот" in line:
        cat_found = True
    if "Пёс" in line or "пёс" in line:
        dog_found = True

if cat_found and not dog_found:
    print("МЯУ")
else:
    print("НЕТ")
