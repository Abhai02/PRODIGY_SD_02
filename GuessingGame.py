import random

def number_guessing_game():
    number = random.randint(1, 100)  # Generates a random number between 1 and 100
    attempts = 0  # Counter for the number of attempts

    print("Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 100. Try to guess it!")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1  # Increment attempt count

            if guess < number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {number} correctly in {attempts} attempts.")
                break  # Exit the loop once guessed correctly
        except ValueError:
            print("Invalid input. Please enter a number.")

# Run the game
number_guessing_game()
