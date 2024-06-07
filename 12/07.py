a = input().split()
i = 0
while len(a) > 1:
    if a[i] == '+':
        a.insert(i - 2, int(a[i - 2]) + int(a[i - 1]))
        del a[i - 1: i + 2]
        i -= 2
    elif a[i] == '-':
        a.insert(i - 2, int(a[i - 2]) - int(a[i - 1]))
        del a[i - 1: i + 2]
        i -= 2
    elif a[i] == '*':
        a.insert(i - 2, int(a[i - 2]) * int(a[i - 1]))
        del a[i - 1: i + 2]
        i -= 2
    else:
        i += 1
print(a[0])