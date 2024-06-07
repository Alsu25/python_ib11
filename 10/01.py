n = int(input())
nums = set(int(x) for x in input().split())
x = int(input())
if any(y != x and x % y == 0 for y in nums):
    print("ДА")
else:
    print("НЕТ")
