import random

"""
snake:- 0
water:- 1
gun:- 2
"""
playerstr = None
player_name = input("Enter player name: ")

while playerstr != "e":

    print("s->Snake\nw->Water\ng->Gun\ne->exit")

    computer = random.choice([0, 1, 2])

    playerstr = input("Enter your choice, (s,w,g,e) : ")

    if playerstr == "e":
        print("Game exited")
        break

    playerdict = {"s": 0, "w": 1, "g": 2}
    reversedict = {0: "Snake", 1: "Water", 2: "Gun"}

    if playerstr not in playerdict:
        print("Invalid choice!")
        continue

    player = playerdict[playerstr]

    print(f"{player_name} chose :- {reversedict[player]}\nComputer chose :- {reversedict[computer]}")

    if computer == player:
        print("It's a Draw!")

    else:

        if computer == 0 and player == 1: 
            print("Computer wins!")

        elif computer == 0 and player == 2: 
            print(f"{player_name} wins!")

        elif computer == 1 and player == 0: 
            print(f"{player_name} wins!")

        elif computer == 1 and player == 2: 
            print("Computer wins!")

        elif computer == 2 and player == 0: 
            print("Computer wins!")

        elif computer == 2 and player == 1: 
            print(f"{player_name} wins!")