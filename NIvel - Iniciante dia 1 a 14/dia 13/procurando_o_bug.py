''' Depurando o codigo a procura do bug '''
# from random import randint

############DEBUGGING#####################

# Describe Problem
#def my_function():
#    ''' Função que mostrar o erro '''
#    for i in range(1, 21):
#        # a função range, sempre desconsidera o valor
#        # alvo, por isso o valor 20 não é contado
#        # Para corrigir o bug, basta acrescentar mais um valor ao range de 1 a 20 + 1 ou 1 a 21
#        if i == 20:
#            print("You got it")
#my_function()

# Reproduce the Bug
#dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
#dice_num = randint(0, 5)
#print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth? "))
# if year >= 1980 and year < 1994:
#     print("You are a millenial.")
# elif year >= 1994:
#     print("You are a Gen Z.")

# # Fix the Errors
# age = int(input("How old are you? "))
# if age > 18:
#     print(f"You can drive at age {age}.")

# # Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(f"Total words: {total_words}")
# print(f"Total pages: {pages}")
# print(f"Total words per page: {word_per_page}")

# #Use a Debugger
# def mutate(a_list):
#     b_list = []
#     for item in a_list:
#         new_item = item * 2
#         b_list.append(new_item)
#     return f"{b_list}"
# 
# print(mutate([1,2,3,5,8,13]))
