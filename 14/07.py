def print_statistics(arr):
    print(len(arr))
    if len(arr) == 0:
        print(0)
        print(0)
        print(0)
        print(0)

    else:
        print(sum(arr) / len(arr))
        print(min(arr))
        print(max(arr))
        arr.sort()
        if len(arr) % 2 == 0:
            n1 = len(arr) // 2
            n2 = n1 - 1
            print((arr[n1] + arr[n2]) / 2)
        else:
            print(arr[(len(arr) // 2)])