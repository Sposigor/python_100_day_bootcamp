''' You are going to write a program that will select a random name from a list of names.
The person selected will have to pay for everybody's food bill '''

import random
# 🚨 Don't change the code below 👇
test_seed = 50
random.seed(test_seed)

# Split string method
names = ['Angela', 'Ben', 'Jenny', 'Michael', 'Chloe', 'Chris', 'Jessica',]
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
num_item = len(names)
random_choice = random.randint(0, num_item - 1)
person_selected = names[random_choice]
print(f'{person_selected} is going to buy the meal today!')
