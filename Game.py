import random

#counters-
#Round Count
rc=0
#Draw count=dc
dc=0
#Computer win count= cw
cw=0
#Player win count=pw
pw=0

#Game-Loop
play=True
while play:
    rc=rc+1
    #Computer will choose one option-
    opt1=("rock", "paper", "scissors")
    bot= random.choice(opt1)

    #Player will choose one-
    player=None
    opt2=("rock", "paper", "scissors", "0")
    print("\nRound:",rc)
    while player not in opt2:
        player = input("1.rock\n2.paper\n3.scissors\nEnter 0 to exit\nChoose any one: ").lower()
    print("Computer choosen :", bot)

    #Logic part-
    if player=="0":
        rc=rc-1
        #Summarize-
        print("\nGame summarize-")
        print("Total round played: ", rc)
        print("Game drawn", dc, "times.")
        print("You win ", pw , " times.")
        print("Computer wins ", cw , " times.")
        play=False
        break
    
    elif player==bot:
        print("Draw")
        dc=dc+1
    elif player== "rock" and bot=="scissors":
        print("You win!")
        pw=pw+1
    elif player=="scissors" and bot=="Paper":
        print("You win!")
        pw=pw+1
    elif player=="paper" and bot=="rock":
        print("You win!")
        pw=pw+1
    else:
        print("You lose!")
        cw=cw+1




