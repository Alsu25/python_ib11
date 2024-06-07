s = input().lower()
st = sorted(list(set(s.replace(" ", ""))))
k = 0
Max = 0
for i in st:
    if s.count(i) > k:
        k = s.count(i)
        Max = i
print(Max)