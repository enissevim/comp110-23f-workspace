"""EX02 - One Shot Wordle."""
__author__ = "730577037"

# create variables for the secret word and the guess
secret_word: str = "python"
guess: str = input(f"What is your {len(secret_word)}-letter guess? ")

# creating emoji's
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

secret_idx: int = 0
emoji: str = ""

# testing whether the guess is the same lenght as the secret word
while len(guess) != len(secret_word):
    guess = input(f"That was not {len(secret_word)} letters! Try again: ")


while secret_idx < (len(secret_word)):
    # show green box
    if guess[secret_idx] == secret_word[secret_idx]:     
        emoji += GREEN_BOX
    else:
        # declare a boolean variable to keep track of whether the guessed character exists anywhere else in the word
        inside: bool = False
        idx: int = 0
        while (idx < (len(secret_word)) and (inside is not True)):
            if guess[secret_idx] == secret_word[idx]:
                inside = True
            else:
                idx += 1
        # show yellow box
        if inside is True:
            emoji += YELLOW_BOX
        # show white box
        else:
            emoji += WHITE_BOX
    # ends infinite loop
    secret_idx = secret_idx + 1
print(emoji)

# finalize the outcomes
if guess == secret_word:
    print("\nWoo! You got it!")
else:
    print("\nNot quite. Play again soon!")