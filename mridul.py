
import random
choices = ["Rock", "Paper", "Scissors"]
computer = random.choice(choices)
cpu_score = 0
player_score = 0
while True:
    player = input("Rock, Paper or Scissors?").capitalize()
## Conditions of Rock,Paper and Scissors
    if player == computer:
        print("Tie!")


    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
            cpu_score+=1
        if computer == "Scissors":
            print("You win!", player, "
elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
            cpu_score+=1
        if computer == "Rock":
            print("You win!", player, "covers", computer)
            player_score+=1

    elif player == "Scissors":
        if computer == "Rock":
            print("Computer wins")
            cpu_score+=1
        if computer == "Paper":
            print("Player wins")
            player_score+=1





