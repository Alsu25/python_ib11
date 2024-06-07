n = int(input())
lst = [int(input()) for _ in range(n)]
p, q = map(int, input().split())
sum = 0
for i in range(p - 1, q):
    sum += lst[i]
print(sum)
