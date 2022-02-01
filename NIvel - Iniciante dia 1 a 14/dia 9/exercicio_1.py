''' You have access to a database of student_scores in the format of a dictionary.
The keys in student_scores are the names of the students and the values are their exam scores.'''

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

# Create an empty dictionary called student_grades.
student_grades = {}

# Write your code below to add the grades to student_grades.👇
for student, score in student_scores.items():
    if score >= 91:
        student_grades[student] = "Outstanding"
    if score >= 81 and score <= 90:
        student_grades[student] = "Exceeds Expectations"
    if score >= 71 and score <= 80:
        student_grades[student] = "Acceptable"
    if score <= 70:
        student_grades[student] = "Fail"


# 🚨 Don't change the code below 👇
print(student_grades)
