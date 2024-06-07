N = int(input())

for _ in range(N):
  line = input()
  if line.startswith("%%"):
    line = line[2:]
  if not line.startswith("####"):
    print(line)
