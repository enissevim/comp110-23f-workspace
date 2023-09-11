"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730577037"

word: str = (input("Enter a 5-character word: "))
if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
single_chr: str = (input("Enter a single character: "))
if len(single_chr) != 1:
    print("Error: Character must be a single character.")
    exit()

word = word.lower()
single_chr = single_chr.lower()

print("Searching for " + single_chr + " in " + word)

count: int = 0


if single_chr == word[0]:
    print(single_chr + " found at index 0")
    count += 1

if single_chr == word[1]:
    print(single_chr + " found at index 1")
    count += 1


if single_chr == word[2]:
    print(single_chr + " found at index 2")
    count += 1


if single_chr == word[3]:
    print(single_chr + " found at index 3")
    count += 1


if single_chr == word[4]:
    print(single_chr + " found at index 4")
    count += 1

if count == 0:
    print("No instances of " + single_chr + " found in " + word)
else:
    if count == 1:
        print(str(count) + " instance of " + single_chr + " found in " + word)
    else:
        print(str(count) + " instances of " + single_chr + " found in " + word)
