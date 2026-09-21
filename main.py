import random
from ast import While


def main():
    player_choice = None
    robot_choice = None
    player_points = 0
    robot_points = 0
    player_win = 0
    robot_win = 0
    Rock = "Rock"
    Paper = "Paper"
    Scissors = "Scissors"
    Rock_win = f"{Rock} > {Scissors}"
    Paper_win = f"{Paper} > {Rock}"
    Scissors_win = f"{Scissors} > {Paper}"

    Rock_lose = f"{Rock} < {Paper}"
    Paper_lose = f"{Paper} < {Scissors}"
    Scissors_lose = f"{Scissors} < {Rock}"


    word_choice = ("Rock", "Paper", "Scissor")

    print("Welcome!\n")

    print("Rock, Paper, Scissors\n")

    while True:

        game = random.choice(["Rock", "Paper", "Scissors"])

        while True:
            guess = input("Guess a hand signal")
            if guess != "Rock" and guess != "Paper" and guess != "Scissors":
                print("Type in Rock, Paper, or Scissors")
                
            else:
                break

        print(f"\nYou chose: {guess}")
        print(f"Bot chose: {game}\n")
            
        if guess == game:
            print("Its a tie!\n")




        if game != guess:
            player_points -= 1
            robot_points += 1
            if player_points < 0:
                player_points = 0
            
            if robot_points == 3:
                robot_points = 3
        print(f"The bot has won a point\n, Your current points: {player_points}\n Robot points: {robot_points}\n Your current win: {player_win}\n Robot win: {robot_win}\n ")
        
        if game == guess.lower():
            player_points += 1
            print(f"You have won a point\n, Your current points: {player_points}\n Robot points: {robot_points}\n Your current win: {player_win}\n Robot win: {robot_win}\n ")
            
        if player_points ==3:
            player_win += 1

        if robot_points == 3:
            robot_win += 1

        if robot_win == 3:
            print ("Robot wins!\n")

        if player_win == 3:
            print("Player wins!\n")




            
                



main()

