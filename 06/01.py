first_list = []
second_list = []
while True:
    num = input()
    if num == "":
        break
    first_list.append(num)
while True:
    num = input()
    if num == "":
        break
    second_list.append(num)
common_numbers = list(set(first_list) & set(second_list))
if len(common_numbers) == 0:
    print("EMPTY")
else:
    for num in common_numbers:
        print(num)
