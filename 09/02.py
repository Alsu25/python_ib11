n = int(input())
data = []
for _ in range(n):
    data.append(input())
search_string = input()
for line in data:
    if search_string in line:
        print(line)
