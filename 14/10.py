def golden_ratio(n):
    res = 1
    for i in range(n - 1):
        res = (res + 1) / res
    return res


n = int(input('n = '))
print(golden_ratio(n))
