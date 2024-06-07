size = int(input ())
strings = []
for j in range (size):
   strings.append(input ())
valid_strings = [string for string in strings if "лук" not in string.lower()]