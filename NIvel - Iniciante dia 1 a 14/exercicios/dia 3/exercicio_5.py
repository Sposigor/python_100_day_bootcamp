# Calculadora do amor

''' You are going to write a program that tests the compatibility between two people.'''

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

text = name1.lower() + name2.lower()
T = text.count('t')
R = text.count('r')
U = text.count('u')
E = text.count('e')
L = text.count('l')
O = text.count('o')
V = text.count('v')
E = text.count('e')
true = T + R + U + E
love = L + O + V + E
soma = str(true) + str(love)
soma = int(soma)
if soma > 90 or soma < 10:
    print(f"Your score is {soma}, you go together like coke and mentos.")
elif soma > 40 and soma < 50:
    print(f"Your score is {soma}, you are alright together.")
else:
    print(f"Your score is {soma}.")
