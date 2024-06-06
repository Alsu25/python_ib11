n = int(input())
cat_found = False
for i in range(n+1):
    line = input()
    if 'кот' in line.lower():
        cat_found = True
        break
if cat_found:
    print('МЯУ')
else:
    print('НЕТ')

