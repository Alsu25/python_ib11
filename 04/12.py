n = int(input())
s = 0
for i in range(n):
    num = int(input())
    if i % 2 == 0:
        s += num
    else:
        s -= num
print(s)
