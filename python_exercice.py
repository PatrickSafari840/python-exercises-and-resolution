Sure, here is the translation of the code you provided:

#---------------------------------------------------------------------------------------------------------------#
#Write a program that uses a function that returns the sum of two integers passed as parameters to the function.

a = 10
b = 30

#a = int(input("Enter the first number: "))
#b = int(input("Enter the second number: "))

def sum(a,b):
   return a+b
     
sum = sum(a,b)
print(sum)
print("-"*100)
#---------------------------------------------------------------------------------------------------------------#

#Write a program with a function that takes two floating point numbers and a character as arguments, and returns a result corresponding to one of the 4 operations applied to its first two arguments, depending on the value of the last, namely: addition for the character +, subtraction for -, multiplication for * and division for / (any character other than the 4 mentioned will be interpreted as an addition). We will take into account the risks of division by zero.

c = 1.5
d = 1.5

#c = float(input("Enter the first number: "))
#d = float(input("Enter the second number: "))

def result(c,d):
    sign = "+"
    #sign = input("Choose an operator ( + , - , * , /): ")
   
    if sign == "+":
        operation_a = c + d
        return operation_a
    elif sign == "-":
        operation_b = c - d
        return operation_b
    elif sign == "*":
        operation_c = c * d
        return operation_c
    elif sign == "/":
        if d == 0 :
            print("This operation is impossible!")
        else:
            operation_d = c / d  
            return operation_d
    else:
       operation_a = c + d
       return operation_a

rs = result(c,d)
print(rs)
print("-"*100)
#---------------------------------------------------------------------------------------------------------------#

#Write a program that uses a function to return the largest of two integers passed as parameters to the function.

e = 10
f = 5
g = 4

#e = int(input("Enter the first number: "))
#f = int(input("Enter the first number: "))
#g = int(input("Enter the first number: "))

def largest(e,f,g):
    if e > f and g :
        return e
    elif f > e and g :
        return f
    elif g > e and f :
        return g

plg = largest(e,f,g)
print(f"The largest number of these three numbers is {plg} :)")
print("-"*100)
#---------------------------------------------------------------------------------------------------------------#

#Write two functions with one integer argument and a boolean return value that will be true if the argument received is a multiple of 2 (for the first function) or a multiple of 3 (for the second function) or false otherwise.

def is_multiple_of_two(number):
    return number % 2 == 0

def is_multiple_of_three(number):
    return number % 3 == 0

j = 10
#j = int(input("Enter a number: "))

result_multiple_of_two = is_multiple_of_two(j)
result_multiple_of_three = is_multiple_of_three(j)

print(f"The number {j} is a multiple of 2: {result_multiple_of_two}")
print(f"The number {j} is a multiple of 3: {result_multiple_of_three}")
print("-"*100)
#---------------------------------------------------------------------------------------------------------------#

 
