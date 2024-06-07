s = input().split()
print('[', end='')
for i in range(len(s)):
    if (i + 1) == len(s):
        print('"' + s[i] + '"', end='')
    else:
        print('"' + s[i] + '"', end=', ')
    i += 1
print(']')