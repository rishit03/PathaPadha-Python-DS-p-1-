import math
import random

print("Press '1' : Stone | '2' : Paper | '3' : Scissors")
user_score = 0
comp_score = 0

for i in range(0,5):
    comp = random.randint(1,3)
    user = int(input("Your Turn : "))

    if(comp==1):
        comp_chose = "Stone"
    elif(comp==2):
        comp_chose = "Paper"
    elif(comp==3):
        comp_chose = "Scissors"
    
    if(comp==1):
        if(user==1):
            user_chose = "Stone"
        elif(user==2):
            user_chose = "Paper"
        elif(user==3):
            user_chose = "Scissors"
            
        print("You chose :",user_chose," Computer chose =",comp_chose,"\n")
            
        if(user==1):
            print("Its a tie!\n")
        elif(user==2):
            print("You win!\n")
            user_score+=1
        elif(user==3):
            print("You lose!\n")
            comp_score+=1

    if(comp==2):
        if(user==1):
            user_chose = "Stone"
        elif(user==2):
            user_chose = "Paper"
        elif(user==3):
            user_chose = "Scissors"
            
        print("You chose :",user_chose," Computer chose =",comp_chose,"\n")
            
        if(user==1):
            print("You lose!\n")
            comp_score+=1
        elif(user==2):
            print("Its a tie!\n")
        elif(user==3):
            print("You win!\n")
            user_score+=1

    if(comp==3):
        if(user==1):
            user_chose = "Stone"
        elif(user==2):
            user_chose = "Paper"
        elif(user==3):
            user_chose = "Scissors"

        print("You chose :",user_chose," Computer chose =",comp_chose,"\n")
            
        if(user==1):
            print("You win!\n")
            user_score+=1
        elif(user==2):
            print("You lose!\n")
            comp_score+=1
        elif(user==3):
            print("Its a tie!\n")

    print ("Your score :",user_score," Computer score =",comp_score,"\n")

if(user_score>comp_score):
    print("Congratulations! You win the game!")
    
elif(user_score<comp_score):
    print("Sorry! You lose the game!")
    
elif(user_score==comp_score):
    print("Its a draw!")

print("Thanks for playing :)")


