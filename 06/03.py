num_english = int(input())
english_students = set()
for i in range(num_english):
    student = input()
    english_students.add(student)

num_german = int(input())
german_students = set()
for i in range(num_german):
    student = input()
    german_students.add(student)

num_both = len(english_students & german_students)
num_only_one = num_english + num_german - 2 * num_both

if num_only_one == 0:
    print("NO")
else:
    print(num_only_one)
