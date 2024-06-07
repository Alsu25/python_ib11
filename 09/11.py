whitelist = set(input() for _ in range(int(input())))
for _ in range(int(input())):
    query = input()
    if query in whitelist:
        print(query)
