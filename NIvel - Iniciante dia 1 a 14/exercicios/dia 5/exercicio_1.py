''' You are going to write a program that calculates the
average student height from a List of heights.'''

# 🚨 Don't change the code below 👇
student_heights = [180, 124, 165, 173, 189, 169, 146]
for n, z in enumerate(student_heights):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
print(f'Input a list of student heights total height = {sum(student_heights)}')
print(f'number of students = {len(student_heights)}')
print(round(sum(student_heights)/len(student_heights)))
