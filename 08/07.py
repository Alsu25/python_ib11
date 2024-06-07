N = int(input())

for i in range(1, N + 1):
  line = input()
  index = line.find("кот")
  if index != -1:
    print(i, index + 1)
