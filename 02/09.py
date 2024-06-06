a = int(input())
b = int(input())
c = int(input())
boys = [a, b, c]
boys.sort(reverse=True)
for boy in boys:
    print(boy)