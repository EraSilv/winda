import random

min = 1
max = 6

roll_again = 'Yes'

while roll_again == 'Yes' or roll_again == 'y':
    print("                                                    Rolling the dice...                                     ",'\n')
    print("                                                     the values are...                                  ")
    print(random.randint(min,max))
    print(random.randint(min,max))
    print("Your total number is ", )

    roll_again = input("Roll the dice again?: ")


