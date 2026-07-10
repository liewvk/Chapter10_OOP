from student import Student


students = [
    Student("Alice", 85, 92),
    Student("Ben", 72, 80),
    Student("Cathy", 90, 95),
    Student("David", 45, 60),
    Student("Ella", 58, 75)
]

print(Student.school_name)
print("=" * len(Student.school_name))

total_score = 0
pass_count = 0
fail_count = 0

for student in students:
    student.display_info()
    print()

    total_score += student.score

    if student.get_result() == "Pass":
        pass_count += 1
    else:
        fail_count += 1

average_score = total_score / len(students)

print("Summary Report")
print("--------------")
print(f"Number of students: {len(students)}")
print(f"Average score: {average_score:.2f}")
print(f"Students passed: {pass_count}")
print(f"Students failed: {fail_count}")
