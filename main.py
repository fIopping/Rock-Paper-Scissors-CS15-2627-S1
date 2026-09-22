import random
from ast import While


def main():
    player_points = 0
    robot_points: int = 0
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

        elif guess == "Rock" and game == "Scissors":
            player_points += 1
            print(f"{Rock_win}")
            print(f"You have won a point\n, Your current points: {player_points}\n Robot points: {robot_points}\n Your current win: {player_win}\n Robot win: {robot_win}\n ")

        elif guess == "Paper" and game == "Rock":
            player_points += 1
            print(f"{Paper_win}")
            print(f"You have won a point\n, Your current points: {player_points}\n Robot points: {robot_points}\n Your current win: {player_win}\n Robot win: {robot_win}\n ")

        elif guess == "Scissors" and game == "Paper":
            player_points += 1
            print(f"{Scissors_win}")
            print(f"You have won a point\n, Your current points: {player_points}\n Robot points: {robot_points}\n Your current win: {player_win}\n Robot win: {robot_win}\n")

        elif guess == "Rock" and game == "Paper":
            robot_points += 1
            print(f"{Rock_lose}")
            print(
                f"Robot has won a point\n, Your current points: {player_points}\n Robot points: {robot_points}\n Your current win: {player_win}\n Robot win: {robot_win}\n")


        elif guess == "Paper" and game == "Scissors":
            robot_points += 1
            print(f"{Paper_lose}")
            print(
                f"Robot has won a point\n, Your current points: {player_points}\n Robot points: {robot_points}\n Your current win: {player_win}\n Robot win: {robot_win}\n")


        elif guess == "Scissors" and game == "Rock":
            robot_points += 1
            print(f"{Scissors_lose}")
            print(
                f"Robot has won a point\n, Your current points: {player_points}\n Robot points: {robot_points}\n Your current win: {player_win}\n Robot win: {robot_win}\n")

        if player_points == 3:
            player_win += 1
            print("You won this round!\n")

        if robot_points == 3:
            robot_win += 1
            print("Robot won this round!\n")



main()