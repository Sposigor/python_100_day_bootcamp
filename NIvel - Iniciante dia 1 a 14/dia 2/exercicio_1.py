# vamos mamipular o tipo de dado

'''
Write a program that adds the digits
in a 2 digit number. e.g. if the input was 35,
then the output should be 3 + 5 = 8
'''

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
####################################
primeiro_numero = two_digit_number[0]
segundo_numero = two_digit_number[1]
soma = int(primeiro_numero) + int(segundo_numero)
soma = str(soma)
print(type(soma))
print(soma)
