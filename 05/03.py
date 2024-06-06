i = 1
while True:
    s = input()
    if s == "СТОП":
        break
    if "кот" in s:
        print(i)
        break
    i += 1
else:
    print(-1)



