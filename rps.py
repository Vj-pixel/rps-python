import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def play_round(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"

def wants_to_play():
    answer = input("Do you want to play Rock, Paper, Scissors? (yes/no): ").lower()
    if answer == "yes" or answer == "y":
        return True
    else:
        print("Maybe next time!(invalid input!)")
        return False

def game():
    user_score = 0
    computer_score = 0
    ties = 0

    if not wants_to_play():
        return  # Exit if the user doesn't want to play

    play_again = True

    while play_again:
        user_choice = input("Enter rock, paper, or scissors: ").lower()
        computer_choice = get_computer_choice()

        result = play_round(user_choice, computer_choice)
        print(f"Computer chose: {computer_choice}\n{result}")

        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1
        else:
            ties += 1

        print(f"Score: You - {user_score} | Computer - {computer_score} | Ties - {ties}")

        play_again_response = input("Play again? (y/n): ").lower()
        play_again = play_again_response == "y"

    print("Thanks for playing!")

# Start the game
name = input("What is your name? ")
print("Hello, " + name + "!")
game()