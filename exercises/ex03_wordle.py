"""EX03 - Structured Wordle!"""
__author__ = "730577037"


# defining a function to determine if the letter guessed is in the secret word
def contains_char(secret_word: str, char: str) -> bool:
    """Indexing throughout the word to see if the character is there."""
    assert len(char) == 1
    idx: int = 0
    found: bool = False
    while idx < len(secret_word):
        if char == secret_word[idx]:
            found = True
        idx += 1

    if found is True:
        return True
    else:
        return False


# defining function to return the correct emoji's for every guess
def emojified(guess: str, secret_word: str) -> str:
    """Output string of emoji's."""
    assert len(guess) == len(secret_word)
    idx: int = 0


    secret_word_idx: int = 0
    emoji: str = ""

    # creating emoji's
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    while idx < len(secret_word):
        # show green box
        if guess[idx] == secret_word[idx]:
            emoji += GREEN_BOX
        else:
            # declare a boolean variable to keep track of whether the guessed character exists anywhere else in the word
            inside: bool = contains_char(secret_word, guess[idx])

            # yellow box
            if inside is True:
                emoji += YELLOW_BOX
            # white box
            else:
                emoji += WHITE_BOX

        idx += 1
        secret_word_idx += 1

    return emoji


# defining function to ask for an input from the use
def input_guess(length: int) -> str:
    """Checking the length of the guess vs the length of the word."""
    guess: str = input(f"Enter a {length} character word: ")

    # making sure the user is entering 5 letter words
    while len(guess) != length:
        guess = input(f"That wasn't {length} chars! Try again: ")
    else:
        return guess


# declaring a function that includes the secret word and allows the program to start
def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    turn: int = 1
    win: bool = False

    # telling the user which turn they are on
    while turn <= 6:
        if win is False:
            print(f"=== Turn {turn}/6 ===")
            new_guess: str = input_guess(len(secret_word))
            results = emojified(new_guess, secret_word)
            print(results)
            if (new_guess == secret_word):
                print(f"You won in {turn}/6 turns!")
                win = True
        turn += 1

    # showing the user that the game ended
    if win is not True:
        print("X/6 - Sorry try again tomorrow!")

if __name__ == "__main__":
    main()