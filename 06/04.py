num_english = int(input())
num_german = int(input())
all_students = set()
for i in range(num_english + num_german):
    student = input()
    all_students.add(student)

num_only_one = len(all_students) - max(num_english, num_german)

if num_only_one == 0:
    print("NO")
else:
    print(num_only_one)
