import random

def play_game():
    print("🎮 Welcome to the Number Guessing Game!")

    # Ask player name
    name = input("Enter your name: ")

    # Difficulty selection
    print("\nChoose difficulty level:")
    print("1. Easy (1–20)")
    print("2. Medium (1–50)")
    print("3. Hard (1–100)")

    difficulty = input("Enter choice (1/2/3): ")

    if difficulty == '1':
        max_range = 20
    elif difficulty == '2':
        max_range = 50
    else:
        max_range = 100

    number = random.randint(1, max_range)
    max_attempts = 7
    attempts = 0
    guessed = False

    print(f"\nGuess a number between 1 and {max_range}. You have {max_attempts} attempts.\n")

    while attempts < max_attempts:
        try:
            guess = int(input("Your guess: "))
            attempts += 1

            if guess < number:
                print("📉 Too low!\n")
            elif guess > number:
                print("📈 Too high!\n")
            else:
                print(f"🎉 Correct! You guessed it in {attempts} attempts.\n")
                guessed = True
                break
        except ValueError:
            print("❌ Please enter a valid number.")

    if not guessed:
        print(f"😞 Sorry! You've used all {max_attempts} attempts. The number was {number}.\n")

    # Log result
    with open("game_results.txt", "a") as file:
        file.write(f"{name} - {'Guessed' if guessed else 'Failed'} in {attempts} attempt(s) on difficulty {difficulty}\n")

    # Replay option
    replay = input("Do you want to play again? (yes/no): ").lower()
    if replay == "yes":
        play_game()
    else:
        print("👋 Thanks for playing!")

# Run the game
play_game()
