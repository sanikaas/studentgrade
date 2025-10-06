# Student Grade Evaluation Program

marks = int(input("Enter marks of the student: "))

if marks >= 90:
    grade = 'A'
elif marks >= 80:
    grade = 'B'
elif marks >= 70:
    grade = 'C'
elif marks >= 60:
    grade = 'D'
else:
    grade = 'Fail'

print("Grade:", grade)

# Student Grade Evaluation Program - Grade Average Branch

marks = []

for i in range(1, 6):
    m = float(input(f"Enter marks for subject {i}: "))
    marks.append(m)

average = sum(marks) / 5

if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B'
elif average >= 70:
    grade = 'C'
elif average >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f"Average Marks: {average:.2f}")
print(f"Grade: {grade}")