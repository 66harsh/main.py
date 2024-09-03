import random

# Tuple for the choices
Choices = ("rock", "paper", "scissors")


def get_player_choice():
    """Get and validate the player's choice."""
    player = None
    
    while player not in Choices:
        player = input("Enter your choice (rock, paper, scissors): ").lower()
    return player


def determine_winner(player, computer):
    """Determine the winner of the game."""
    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "You win!"
    else:
        return "You lose!"

def main():
    while True:
        player = get_player_choice()
        computer = random.choice(Choices)
        
        print(f"Player choice: {player}")
        print(f"Computer choice: {computer}")
        
        result = determine_winner(player, computer)
        print(result)
        
        play_again = input("Play again? (y/n): ").lower()
        if play_again != "y":
            break

    print("Thanks for playing!")

if __name__ == "__main__":
    main()
