import random
options=("rock","paper","scissors") 
running=True

while running:
    player=None
    computer=random.choice(options)

    while player not in options:
        player=input(" enter the choic in options (rock,paper,scissors) =")
        print(f"player:{player}")
        print(f"computer:{computer}")
        if player=="rock" and computer=="scissors":
            print("you won!")
        elif player=="scissors" and computer=="paper":
            print("you won !")
        elif player=="paper"  and computer=="scissors":
            print("you won !")
        elif player==computer:
            print("its a tie !")    
        else:
            print("you lose match try again !")
        playmore=input("play again?(y/n)") 
        if playmore=="n":
            running=False
print("thank you visit again web")