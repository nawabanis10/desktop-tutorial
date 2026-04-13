# 🎲 Dice Roller Game
## 📌 Description
This is a simple Dice Roller game built in Python. It generates a random number between 1 and 6 when the user rolls the dice.

import random
import numbers

print("=== welcome to Dice Roller ===")

user_score_1=0
user_score_2=0
user_score_3=0
user_score_4=0


while True:
    user=input("press enter to: (Roll dice or exit:)").lower()
    if user == 'exit':
        break

    user_dice_1=random.randint(1 , 6)
    user_dice_2=random.randint(1 , 6)
    user_dice_3=random.randint(1 , 6)
    user_dice_4=random.randint(1 , 6)



 
    print(f"\n user_dice_1 is: {user_dice_1} \n user_dice_2: {user_dice_2} \n user_dice_3: {user_dice_3} \n  user_dice_4: {user_dice_4}")
 
    if user_dice_1 > user_dice_2 and user_dice_1 > user_dice_3 and user_dice_1 > user_dice_4:
        print("user_1 win this round")
        user_score_1=user_score_1 +1

    elif user_dice_2 > user_dice_1 and user_dice_2 > user_dice_3 and user_dice_2 > user_dice_4:
        print("user_2 win this round")
        user_score_2=user_score_2 +1
    
    elif user_dice_3 > user_dice_1 and user_dice_3 > user_dice_2 and user_dice_3 > user_dice_4:
        print("user_3 win this round")
        user_score_3=user_score_3 +1

    elif user_dice_4 > user_dice_1 and user_dice_4 > user_dice_2 and user_dice_4 > user_dice_3:
        print("user_4 win this round")
        user_score_4=user_score_4 +1

    else:
        print("it is draw")
    
print("your final score is :",user_score_1)
print("your final score is :",user_score_2)
print("your final score is :",user_score_3)
print("your final score is :",user_score_4)

 
if user_dice_1 > user_dice_2 and user_dice_1 > user_dice_3 and user_dice_1 > user_dice_4:
    print(f"Congratulation user_1 is final winner {user_dice_1}")

elif user_dice_2 > user_dice_1 and user_dice_2 > user_dice_3 and user_dice_2 > user_dice_4:
    print(f"Congratulation user_2 is final winner {user_dice_2}")

elif user_dice_3 > user_dice_1 and user_dice_3 > user_dice_2 and user_dice_3 > user_dice_4:
    print(f"Congratulation user_3 is final winner {user_dice_3}")

elif user_dice_4 > user_dice_1 and user_dice_4 > user_dice_2 and user_dice_4 > user_dice_3:
    print(f"Congratulation user_4 is final winner {user_dice_4}")


else:
    print("Game over !")
