N = int(input())
tips = []

for _ in range(N):
  tip = input()
  tips.append(tip)

for tip in tips:
  if tip.startswith(("не ", "Не ")):
    print(tip[3:])
  else:
    print(tip)
