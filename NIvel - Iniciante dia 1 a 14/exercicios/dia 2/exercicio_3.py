# Vamos criar um converso de idada

''' Create a program using maths and f-Strings that tells
us how many days, weeks, months we have left if we live
until 90 years old. '''

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
days = ((90 * 365) - (int(age) * 365))
weeks = ((90 * 52) - (int(age) * 52))
month = ((90 * 12) - (int(age) * 12))
print(f' You have {days} days, {weeks} weeks, and {month} months left.')