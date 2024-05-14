import random  # Importing the random module to generate computer's choice
import os  # Importing the os module to clear the screen

def determine_winner(player_choice, computer_choice):
    """
    Determines the winner of the game based on player's and computer's choices.
    
    Args:
        player_choice (str): The choice made by the player ('rock', 'paper', or 'scissors').
        computer_choice (str): The choice made by the computer ('rock', 'paper', or 'scissors').
    
    Returns:
        str: A string indicating the result of the game.
    """
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    """
    The main function to run the Rock, Paper, Scissors game.
    """
    choices = ["rock", "paper", "scissors"]  # List of valid choices
    
    while True:
        print("\nWelcome to Rock, Paper, Scissors!")
        player_choice = input("Enter your choice (rock/paper/scissors): ").lower()
        
        if player_choice not in choices:
            print("Invalid choice! Please enter 'rock', 'paper', or 'scissors'.")
            continue
        
        computer_choice = random.choice(choices)  # Randomly selects computer's choice
        print(f"\nYou chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(player_choice, computer_choice)  # Determines the winner
        print(result)
        
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again == "yes":
            os.system('cls')  # Clears the screen for a new game on Windows
            continue

        elif play_again == 'no':
            os.system('cls')  # Clears the screen before exiting on Windows
            print("Thanks for playing!")
            break

main()  # Calls the main function to start the game

