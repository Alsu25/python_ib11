n = int(input())
data = []
for _ in range(n):
    data.append(input())
m = int(input())
search_strings = []
for _ in range(m):
    search_strings.append(input())
for line in data:
    found_all = True
    for search_string in search_strings:
        if search_string not in line:
            found_all = False
            break
    if found_all:
        print(line)
