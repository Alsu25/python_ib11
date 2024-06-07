string = input()
words = string.split()
result = []
for i in range(2, len(words), 3):
    result.append(words[i])

print(' '.join(result))
