list = []
M, N = int(input()), int(input())
for i in range(M):
  line = input()
  list.append(line)
for j in range(N):
  line = input()
  f = 0
  for k in range(len(list)):
    if list[k] == line:
        print("YES")
        f = 1
        break
  if f == 0:
    print("NO")