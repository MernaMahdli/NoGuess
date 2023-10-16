def number_guessing_game():
    """
    A simple number guessing game where the user guesses a number between 0 and 100.
    """

    print("Please guess a number between 0 and 100!")

    low = 0
    high = 100
    medium = (low + high) // 2
    state = True

    while state:
        print("Is your guess " + str(medium) + "?")
        guess = input("Enter 'h' if the guess is too high, 'l' if it's too low, or 'YES' if it's the correct number: ")

        if guess == "YES":
            print("Alright! Your guess was: " + str(medium) + " :D")
            state = False
        elif guess == "h":
            high = medium
            medium = (high + low) // 2
        elif guess == "l":
            low = medium
            medium = (high + low) // 2
        else:
            print("Incorrect input. Please try again :)")

# Call the function to play the number guessing game
number_guessing_game()
