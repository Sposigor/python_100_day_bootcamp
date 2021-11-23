''' Prime numbers are numbers that can only be cleanly divided by themselves and 1. '''

#Write your code below this line 👇
def prime_checker(number):
    ''' verifica se é numero primo '''
    e_primo = True
    for i in range(2, number):
        if number % i == 0:
            e_primo = False
    if e_primo:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
