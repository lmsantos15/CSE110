# Week 08 sample

secret_word = "jean"

# This code gives us a hint
print("Your hint is: ", end="")
for letter in secret_word:
    print("_ ", end="") # end= indicates that the end character has to be identified by whitespace and not a newline.
print()

guess = input("What is your guess? ")
guess_count = 1 # Couns how many guess you have made

while guess != secret_word: # The != (negative condition) will loop the secret word until they guessed it right
    guess_length = len(guess)
    for i in range(guess_length):
        letter = guess[i] # Looks at each letter of the guess [i]
        
        if letter == secret_word[i]:
            print(letter.upper())
        
        elif letter in secret_word:
            print(letter.lower())

    guess = input("What is your guess? ")
    guess_count += 1 # += adds the guesses you have made


print(f"You guessed it in {guess_count} guesses.")




