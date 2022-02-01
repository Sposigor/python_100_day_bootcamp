# Vamos fazer uma calculadora de IMC

''' Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.'''

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
height = float(height)
weight = float(weight)
print(int(weight / height ** 2))
