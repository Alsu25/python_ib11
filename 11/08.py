s = input().split('?')
del s[0]
s = ''.join(s)
s = str(s)
s = s.split('&')
slovar = {}
for i in s:
    current = i.split('=')
    slovar[current[0]] = current[1]
print(slovar[input()])