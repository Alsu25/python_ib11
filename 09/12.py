n, total = map(int, input().split())
errors = []
actual_total = 0
for i in range(n):
    price, quantity, actual_price = map(int, input().split('=')[0].split('*'))
    if actual_price != price * quantity:
        errors.append(i + 1)
    actual_total += actual_price
if actual_total != total:
    errors.append('Total')
print(total - actual_total)
for error in errors:
    print(error)
