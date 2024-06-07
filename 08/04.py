n = int(input())
vert = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
k = 0

for i in range(n, 0, -1):
    for j in vert[0:n]:
        print(j, i, sep='', end=' ')
        if j == vert[n - 1]:
            print()