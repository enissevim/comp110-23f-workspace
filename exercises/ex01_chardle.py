"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730577037"

word = (input("Enter a 5-character word: ")).lower()
if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
single_chr = (input("Enter a single character: ")).lower()
if len(single_chr) != 1:
    print("Error: Character must be a single character.")
    exit()


print("Searching for " + single_chr + " in " + word)

count = 0

if single_chr in word[0]:
    print(single_chr + " found at index 0")
    count += 1

if single_chr in word[1]:
    print(single_chr + " found at index 1")
    count += 1


if single_chr in word[2]:
    print(single_chr + " found at index 2")
    count += 1


if single_chr in word[3]:
    print(single_chr + " found at index 3")
    count += 1


if single_chr in word[4]:
    print(single_chr + " found at index 4")
    count += 1

if count == 0:
    print(str(count) + " instance of " + single_chr + " found in " + word)
else:
    print(str(count) + " instance of " + single_chr + " found in " + word)