''' You are going to write a program that calculates
the highest score from a List of scores.'''


# 🚨 Don't change the code below 👇
student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
for n, z in enumerate(student_scores):
    student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
max_score = 0
for i, z in enumerate(student_scores):
    if student_scores[i] > max_score:
        max_score = student_scores[i]
print(f'The highest score is {max_score}')
