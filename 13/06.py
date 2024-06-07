d = {}
for i in s:
    if i not in d:
        d[i] = 0
k = list(d.keys())
for i in s:
    c = 0
    for j in k:
        if i == k[c]:
            d[j] += 1
            print(d[j], end=' ')
        c += 1
