n = int(input())
lines = []
for _ in range(n):
    lines.append(input())
letter_number = int(input())
for line in lines:
    if len(line) >= letter_number:
        print(line[letter_number - 1], end='')
