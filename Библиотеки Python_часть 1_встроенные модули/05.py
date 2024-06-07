import math
import datetime as dt

birth = list(map(int, input().split(".")))
birth = dt.date(birth[2], birth[1], birth[0])
now = list(map(int, input().split(".")))
now = dt.date(now[2], now[1], now[0])

ans1 = round(math.sin((2 * math.pi * (now - birth).days) / 23) * 100, 2)
ans2 = round(math.sin((2 * math.pi * (now - birth).days) / 28) * 100, 2)
ans3 = round(math.sin((2 * math.pi * (now - birth).days) / 33) * 100, 2)
print(ans1)
print(ans2)
print(ans3)