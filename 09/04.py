n = int(input())
parts = []
for _ in range(n):
    parts.append(input())
m = int(input())
indices = []
for _ in range(m):
    indices.append(int(input()) - 1)
for index in indices:
    print(parts[index])
