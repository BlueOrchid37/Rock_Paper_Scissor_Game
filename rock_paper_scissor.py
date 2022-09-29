#Rock Paper Scissor Game

import random
choiceList=["rock", "paper", "scissor"]
while True:
    comCount=0
    userCount=0
    userChoice=int(input('''
    Play Game?
    1. Yes |Play
    2. No  |Exit
    '''))
    if userChoice==1:
        for i in range(1,6):
            userInput=int(input('''
            Enter your Choice:
            1. Rock
            2. Paper
            3. Scissor
            '''))
            if userInput==1:
                userValue="rock"
            elif userInput==2:
                userValue="paper"
            elif userInput==3:
                userValue="scissor"
            else:
                print("Invalid Input")
            systemChoice=random.choice(choiceList)
            if(userValue=="rock" and systemChoice=="rock") or (userValue=="paper" and systemChoice=="paper") or (userValue=="scissor" and systemChoice=="scissor"):
                print("Your Choice: ", userValue)
                print("Computer Choice: ", systemChoice)
                print("Tie")
                userCount=userCount+1
                comCount=comCount+1
            elif(userValue=="rock" and systemChoice=="scissor") or (userValue=="paper" and systemChoice=="rock") or (userValue=="scissor" and systemChoice=="paper"):
                print("Your Choice: ", userValue)
                print("Computer Choice: ", systemChoice)
                print("You Won")
                userCount=userCount+1
            else:
                print("Your Choice: ", userValue)
                print("Computer Choice: ", systemChoice)
                print("Computer Won")
                comCount=comCount+1

            
        if userCount==comCount:
                print("Computer Score: ", comCount)
                print("Your Score: ", userCount)
                print("Series Draw")
        elif userCount>comCount:
                print("Computer Score: ", comCount)
                print("Your Score: ", userCount)
                print("You Won")
        else:
                print("Computer Score: ", comCount)
                print("Your Score: ", userCount)
                print("Computer Won")
    else:
        break