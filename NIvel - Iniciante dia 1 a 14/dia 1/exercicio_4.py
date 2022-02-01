# Vamos usar algumas variaveis

''' Write a program that switches the values stored in the variables a and b. '''

a = input("a: ")
b = input("b: ")
print("a:", b)
print("b:", a)

# Ou temos essa possibilidade

a = input("a: ")
b = input("b: ")

c = a
a = b
b = c

print("a:", a)
print("b:", b)
