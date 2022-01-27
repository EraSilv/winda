#--------------------------------------------- From book Easy way to code in Python------------------------------------------------
# Num ---------------------1------------------------------

# import random
# num = random.randint(0 , 1000)
# flag = True
# guess = 0

# print("Guess my num 0 - 20: " , end= " ")
# while flag == True:
#     guess = input( )
#     if float(guess) > 20:
#         print("Out of digits! Enter only 0 - 20")
#         break
#     if not guess.isdigit():
#         print("Invalid! Enter only digits! 0 - 20")
#         break
#     elif int(guess) < num:
#         print("Ur number is smaller! Try again!", end= " ")
#     elif int(guess) > num:
#         print("Ur number is larger! Try again!", end= " ")
#     else:
#         print(f"Correct! My number was {guess}")
#         flag = False


# Num ---------------------2------------------------------
# --------------------------------------List-----------------------------------
##--------In other programming languages a list is often called an “array”

## quarter = ['Jan', 'Feb', 'Mart']
## quarter.append('April')
## quarter2 = ['May', 'June', 'July']
## quarter.extend(quarter2)
## quarter.insert(0,'December')
## quarter.remove('December')
## quarter.pop(0)
## quarter.reverse()
## print(len(quarter))

# Top = ['Sevban', 'Kemal', 'Husein', 'Selim']
# Pidors = ['Bektash', 'Chelik', 'Tunahans']

# print('Top list:', Top)
# print(' Top elements: ', len(Top))
# Top.append('Taksim')
# print('Appended: ', Top)
# print("Last item removed: ", Top.pop())
# print('Top list: ', Top)
# Top.extend(Pidors)
# print("Extended: ", Top)
# Top.pop(4)
# print("Item removed or killed: ", Top)
# Top.pop(4)
# print("Slice removed or killed: " , Top)




##### Num ---------------------3------------------------------ ####

#Tuple

# months = ("Jan", "Feb",'Mart','Apr',"May",'June','July','Aug','Sept','Oct','Nov','Dec')
# print('Months: ', type(months))
# print('Months of the year: ' , months)
# print('No. of the months in a year: ' , len(months))
# print('Start months of year: ', months[0])

# user = ('Era', 'Yrysbaev', 'Dubai', '555-3536')
# print('Name: ', user[0], user[1])
# print('Phone:', user[3])


##### Num ---------------------4------------------------------ ####
# --------------------------------------Set---------------------------------

# band_wolf = {'Alphas', 'Betas', 'Charlies', 'Golden Down', ' Death'}
# # band_wolf.add('Gamma') #adds one item
# # band_wolf.update({'Gamma', 'Bravo','Silver'})
# # band_wolf.pop()
# # band_wolf.discard('Alphas')
# band_wolf2 = {'Betas', 'Bunnies', 'FireFoxes', 'Charlies', ' Dark Edge'}
# # band_wolf4 = band_wolf.difference(band_wolf2)
# # band_wolf3 = band_wolf.intersection(band_wolf2)
# # print("Difference: ", band_wolf4)
# # print("New bands were added:", band_wolf)

# print("Does Alphas in the tournament?: ", 'Alphas' in band_wolf)
# print(" Is Inazuma 11 Alphas opponents?: ", 'Inazuma 11 ' in band_wolf)
# tournament = band_wolf.intersection(band_wolf2)
# teams = list(tournament)
# print("Teams on the Tournament: ", teams)
# print("First team on the tournament: ", teams[1])



##### Num ---------------------5------------------------------ ####
# -----------------------Dictionary--------------------------------------

### a dictionary is often called an “associative array”.

# info = {
#     'name':'Era',
#     'programm':'Python',
#     'sys': 'Win'
# }
# print('Info:', type(info))
# print("Dictionary: ", info)
# print('\nProgram : ', info['programm'])
# print("\n Keys: ", info.keys())
# del info['name']
# info['user'] = 'Tom'
# print("\nDictionary: ", info)
# print("\nIs there a 'name' key?: ", 'name' in info)



# quarter = ['Jan', 'Feb', 'March', 7]
# print('\n',quarter)
# quarter[1] = 'April'
# print('\n',quarter)
# del quarter[3]
# print("First month is : ", quarter[0])
# print("Second month is : ", quarter[1])
# print("Third month is : ", quarter[2])

# coords = [[1,2,3],[4,5,6]]
# print("\nTop left 0,0: ", coords[0][0])
# print("\nBottom right 1,2: ", coords[1][2])

# print("\nSecond month first letter: ", quarter[1][0])
