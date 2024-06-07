throws = input()
max_count = 0
current_count = 0

for throw in throws:
  if throw == 'о':
    current_count += 1
    max_count = max(max_count, current_count)
  else:
    current_count = 0

print(max_count)
