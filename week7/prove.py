# 07 Prove: Assignment Milestone

print()
magic_word = "safari"

continue_playing = "yes"

# Hitting "YES" will keep the ball rolling
while continue_playing.lower() == "yes":

    # This variable will track their attempts
    guess_count = 0

    guess = -1

    # Will keep going as long as they don't have the right one
    while guess != magic_word:
        guess = input("What is your guess? ")
        guess_count = guess_count + 1

        if guess != magic_word:
            print("Your guess was not correct. \n")
       
        else:
            print("You guessed it! \n")

    # When they answered it correctly
    print(f"It took you {guess_count} guesses")
    print()

    continue_playing = input("Would you like to play again (yes/no)? ")
print()
print("Thank you for playing. Goodbye.")
print()
# Been trying to see how I can make it work like the one that have those hints and underscored, but I can't seem to do it.
# Will try to research further.
# Thank you.