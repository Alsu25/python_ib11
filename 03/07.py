low = 1
high = 1000

while low <= high:
    mid = (low + high) // 2
    print(mid)
    answer = input()
    if answer == '>':
        low = mid + 1
    elif answer == '<':
        high = mid - 1
    else:
        break
