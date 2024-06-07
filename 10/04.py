n = int(input())
strings = []
for _ in range(n):
    strings.append(input())

strings.sort(key=lambda x: (len(x), x))

for string in strings:
    print(string)
