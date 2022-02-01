# Calculadora de IMC

''' Write a program that interprets the Body Mass
Index (BMI) based on a user's weight and height. '''

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = round(weight / (height * height))

if BMI <= 18.5:
    print(f"Your BMI is {BMI}, you are underweight.")
elif BMI > 18.5 and BMI <= 25:
    print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI > 25 and BMI <= 30:
    print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI > 30 and BMI <= 35:
    print(f"Your BMI is {BMI}, you are obese.")
elif BMI > 35:
    print(f"Your BMI is {BMI}, you are clinically obese.")
