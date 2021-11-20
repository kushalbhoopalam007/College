"""
Task-2 a)Write a python program to print the multiplication table for the given number?
"""

num= int(input("Enter a number: "))
print('\nMultiplication table for given number',num,'is\n')
for i in range(1,11):
    print(num,'x',i,'=',num*i)

