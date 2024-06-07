max_length = int(input())
N = int(input())

for _ in range(N):
  headline = input()
  if len(headline) > max_length:
    headline = headline[:max_length - 3] + "..."
  print(headline)
