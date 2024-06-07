n = int(input())
pupils = []
for i in range(n):
    pupils.append(input())
for pupil in pupils:
    print(pupil)
print()
for pupil in pupils:
    if pupil[-1] in ['4', '5']:
        print(pupil)
