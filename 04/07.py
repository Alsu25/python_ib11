n = int(input())

divisors = []
for i in range(1, n + 1):
  if n % i == 0:
    divisors.append(i)

print(*divisors)

if len(divisors) == 2:
  print("ПРОСТОЕ")
else:
  print("НЕТ")
