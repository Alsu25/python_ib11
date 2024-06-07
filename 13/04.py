a = int(input())
spis = {}
for i in range(a):
    b = input().split()
    h = (b[0][:len(b[0]) - 1], b[-1][:len(b[-1]) - 1])
    if h in spis:
        spis[h] += 1
    else:
        spis[h] = 1
print(max(spis.values()))
