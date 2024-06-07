client = []
procent = []
n = int(input())
for i in range(n):
    client.append(int(input()))
    print(client[i])
print()
for i in range(n):
    procent.append(client[i] * 3)
for i in procent:
    print(i)
