def is_valid_pyramid(sides):
    if len(sides) == 1:
        return True
    if sides[0] > sides[1]:
        return False
    return is_valid_pyramid(sides[1:])

def build_pyramid(sides):
    if not is_valid_pyramid(sides):
        return "НЕТ"
    pyramid = []
    while sides:
        if sides[0] <= sides[-1]:
            pyramid.append(sides[0])
            sides = sides[1:]
        else:
            pyramid.append(sides[-1])
            sides = sides[:-1]
    return ' '.join(map(str, pyramid))

n = int(input())
for _ in range(n):
    sides = list(map(int, input().split()))
    print(build_pyramid(sides))
