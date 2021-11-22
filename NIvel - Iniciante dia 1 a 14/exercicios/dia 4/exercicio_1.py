''' You are going to write a virtual coin toss program.
It will randomly tell the user "Heads" or "Tails".'''

import random

#Remember to use the random module
#Hint: Remember to import the random module first. 🎲

# 🚨 Don't change the code below 👇
test_seed = random.randint(0, 999999)
random.seed(test_seed)
# 🚨 Don't change the code above 👆 It's only for testing your code.

#Write your code below this line 👇

moeda = random.randint(0, 1)
print(moeda)
if moeda == 0:
    print("Heads")
else:
    print("Tails")
    
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
 
print(dirty_dozen[1][1])
print(dirty_dozen) 
print(dirty_dozen[0])
print(dirty_dozen[1])
print(dirty_dozen[1][2])
print(dirty_dozen[1][3])