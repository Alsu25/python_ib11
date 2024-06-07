numbers = [int(i) for i in input().split()]
left, right = [int(i) for i in input().split()]
numbers = numbers[left:right + 1]
print(sum(numbers))