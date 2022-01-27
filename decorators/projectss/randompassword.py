from ast import Pass
import random
from re import A
from string import punctuation

#A function do shuffle all the characters of a string
def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)

#Main program starts here
uppercaseLetter1=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter2=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
#Generate more characters here
lowercaseLetter1=chr(random.randint(97,122)) #Generate a random lowercase letter (based on ASCII code)
lowercaseLetter2=chr(random.randint(97,122))

digit1 = chr(random.randint(48,57))  #Generate a random digit from 0-9
digit2 = chr(random.randint(48,57))


punctuationSign1 = chr(random.randint(32,152)) #Generate a random punctuation sign
punctuationSign2 = chr(random.randint(32,152))

#Generate password using all the characters, in random order

password = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2 + digit1 + digit2 + punctuationSign1 + punctuationSign2
password = shuffle(password)
print(password)