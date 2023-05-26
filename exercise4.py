# Project on Rock Paper Scissors
# rule of the game: rock beats scissors, scissors beat paper and paper beats rock

# import random

# print()
# print("welcome to rock, paper and scissors game")
# choice_list = ("rock", "paper", "scissors")
# player_choice = input("Enter your choice ")

# computer_choice = random.choice(choice_list)

# print("you have selected"  + player_choice)
# print("the computer have selected " + computer_choice)


import random

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid input. Please try again.")

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print("Let's play Rock Paper Scissors!")
    play_again = "y"
    user_score = 0
    computer_score = 0
    while play_again == "y":
        print("------------------------------------")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        print(determine_winner(user_choice, computer_choice))
        result = determine_winner(user_choice, computer_choice)
        print(result)
        if result == "You win!":
            user_score += 1
            print(f"Your score: {user_score}")
            print(f"Computer score: {computer_score}")
        elif result == "Computer wins!":
            computer_score += 1
            print(f"Your score: {user_score}")
            print(f"Computer score: {computer_score}")
        play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != "y":
            print("Thanks for playing! Goodbye.")


play_game()


