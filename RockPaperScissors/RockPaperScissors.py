import random

# Function to get the user's choice
def getUserChoice():
    choice = input("Enter a choice (Rock(r), Paper(p), Scissors(s)): ")
    choice = choice.lower()
    while choice not in ['r', 'p', 's']:
        print("Invalid choice. Please try again.")
        choice = input("Enter a choice (Rock(r), Paper(p), Scissors(s)): ").lower()
    return choice

# Function to get the computer's choice
def getComputerChoice():
    choices = ['r', 'p', 's']
    return random.choice(choices)

# Function to print choice
def fullnameChoice(choice):
    if choice == 'r':
        return 'Rock'
    elif choice == 'p':
        return 'Paper'
    elif choice == 's':
        return 'Scissors'

# Function to choose the winner
def chooseWinner(userChoice, computerChoice):
    if userChoice == computerChoice:
        return "Tie."
    elif (userChoice == 'r' and computerChoice == 's') or (userChoice == 'p' and computerChoice == 'r') or (userChoice == 's' and computerChoice == 'p'):
        return "You win."
    else:
        return "You lose."

# Rock smashes Scissors. Paper covers
# Rock. Scissors cut Paper.

# Function to print long result explanation
def longResult(userChoice, computerChoice):
    if (userChoice == 'r' and computerChoice == 'p') or (userChoice == 'p' and computerChoice == 'r'):
        return 'Paper covers Rock.'
    elif (userChoice == 'r' and computerChoice == 's') or (userChoice == 's' and computerChoice == 'r'):
        return 'Rock smashes Scissors.'
    elif (userChoice == 's' and computerChoice == 'p') or (userChoice == 'p' and computerChoice == 's'):
        return "Scissors cut Paper."
        
# Function to play the game
def playGame():
    userScore = 0
    computerScore = 0

# Game loop
    while True:
        userChoice = getUserChoice()
        computerChoice = getComputerChoice()
        print("You chose " + fullnameChoice(userChoice) + ", computer chose " + fullnameChoice(computerChoice) + '.', end=' ')
        
        result = chooseWinner(userChoice, computerChoice)
        if result != "Tie.":
            print(longResult(userChoice, computerChoice), end=' ')
        print(result)

# Score count
        if result == "You win.":
            userScore += 1
        elif result == "You lose.":
            computerScore += 1

# Check if play again
        playAgain = input("Play again? (y/n): ")
        if playAgain.lower() != 'y':
            break

# Print final scores
    print("Final Scores:")
    print("You:", userScore)
    print("Computer:", computerScore)

# Play the game
playGame()
