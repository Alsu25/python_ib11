count_days = 0
count_weeks = 0
while True:
  temp = float(input())
  if temp >= 22.0:
    break
  count_days += 1
  if count_days % 7 == 0:
    count_weeks += 1
print(count_weeks)
