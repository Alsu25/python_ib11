n = int(input())
iq = [int(input()) for _ in range(n)]
avg = 0
for i in range(n):
    avg = (avg*i + iq[i]) / (i+1)
    if iq[i] > avg:
        print('>')
    elif iq[i] < avg:
        print('<')
    else:
        print('0')
