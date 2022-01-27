import random

User1 = 'Man'
User2 = 'Woman'


ManScore = 0
WomanScore = 0

# У каждого кубика шесть возможных значений

dice1 = [1,2,3,4,5,6]
dice2 = [1,2,3,4,5,6]

def PlayDiceGame():
    # Оба участника, Анна и Алекс, бросают кубик, используя метод shuffle
    for i in range(5):
        #оба кубика встряхиваются 5 раз
        random.shuffle(dice1)
        random.shuffle(dice2)
        # использование метода choice для выбора случайного значения
    firstNumber = random.choice(dice1)
    secondNumber = random.choice(dice2)
    return firstNumber + secondNumber


print("Игра в кости использует модуль random\n")
        


#Давайте сыграем в кости три раза


for i in range(3):
    # определим, кто будет бросать кости первым
    #генерация случайного числа от 1 до 100, включая 100
    ManTossNumber = random.randint(1,100)
    #генерация случайного числа от 1 до 100, не включая 101
    WomanTossNumber = random.randint(1,101) 

    if ManTossNumber > WomanTossNumber:
        print("Man выиграл жеребьевку.")
        ManScore = PlayDiceGame()
        WomanScore = PlayDiceGame()
    else:
        print("Woman выигралa жеребьевку.")
        ManScore = PlayDiceGame()
        WomanScore = PlayDiceGame()
    if (ManScore > WomanScore):
        print(f"Алекс выиграл игру в кости. Финальный счет Man:{ManScore}  Финальный счет Woman:{WomanScore}","\n")
    else:
        print(f"Алекс выиграл игру в кости. Финальный счет Woman:{WomanScore}  Финальный счет Man:{ManScore}","\n")

