message = input()
codes = []
for char in message:
    codes.append(str(ord(char)))
print(",".join(codes))