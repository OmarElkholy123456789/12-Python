import random

def user_choice():
    """Create a function which takes in the user choice and returns the 
    user choice to the main play game function."""
    choices = ["paper", "scissors", "rock"]

    while True:
        user_choice = input("Please enter your choice of weapon from either paper, scissors, or rock - ").lower()

        if user_choice not in choices:
            print("Invalid choice. Please try again.")

        else:
            return user_choice
        
def computer_choice():
    """Function which gets the computers choice of weapon in the game of 
    paper, scissors, ric. Will then return the choice value to the game 
    function."""
    choices = ["paper", "scissors", "rock"]
    computer_choice = random.choice(choices)
    return computer_choice

def determine_winner(user_pick, computer_pick):
    """Function which takes in the computers choice and the users choice, 
    compares then returns the overall winner."""
    if user_pick == computer_pick:
        print("It's a tie!")
    elif (user_pick == "rock" and computer_pick == "scissors") or \
        (user_pick == "scissors" and computer_pick == "paper") or \
        (user_pick == "paper" and computer_pick == "rock"):
        return "You win!"
    else:
        return "Computer wins!"
    
def play_game():
    """Function which runs the entire program, will run different functions
    and then returns the winner and asks the user if they want to play
    again."""
    while True:
        user_pick = user_choice()
        computer_pick = computer_choice()

        result = determine_winner(user_pick, computer_pick)

        print(" ")
        print(f"Your choice: {user_pick}")
        print(f"Computers choice: {computer_pick}")
        print(f"Overall result: {result}")

        print("Do you want to play again? Enter y/n below.")
        play_again = input("Enter your decision here (y/n): ")

        if play_again == "n":
            print("Thanks for playing!")
            break
        elif play_again == 'y':
            play_game()
        else:
            print("Please enter y/n")
            play_again = input("Enter your decision here (y/n): ")

play_game()