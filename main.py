import random
from ast import While


def main():
    player_points = 0
    robot_points = 0
    player_win = 0
    robot_win = 0
    Rock = None
    Paper = None
    Scissors = None
    Rock_win = Rock > Scissors
    Paper_win = Paper > Rock
    Scissors_win = Scissors > Paper
    Rock_lose = Rock < Paper
    Paper_lose = Paper < Scissors
    Scissors_lose = Scissors < Rock


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

