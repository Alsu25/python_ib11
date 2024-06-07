a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
c = 0
for i in range(b[0], b[1] + 1):
    c += a[i] * a[i]
print(c)