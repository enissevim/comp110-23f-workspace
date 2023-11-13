"""EX06: Dictionary Functions."""
__author__ = "730577037"


def invert(orig: dict[str, str]) -> dict[str, str]:
    """Takes the values and keys of a dictionary and swaps them."""    
    output: dict[str, str] = {}
    for key in orig:
        if orig[key] in output:
            raise KeyError("Sorry, each of the key values must be unique.")
        output[orig[key]] = key
    return output


def favorite_color(col: dict[str, str]) -> str:
    """Returns a string with the most frequent color in the dictionary."""
    output: str = ""
    i: int = 0
    color_dict: dict[str, int] = {}
    for key in col:
        color = col[key]
        if color in color_dict:
            color_dict[color] += 1
        else:
            color_dict[color] = 1
        if color_dict[color] > i:
            i = color_dict[color] 
            output = color
    return output


def count(freq: list[str]) -> dict[str, int]:
    """Counts the frequency of each value."""
    occur_dict: dict[str, int] = {}
    for item in freq:
        if item in occur_dict:
            occur_dict[item] += 1
        else:
            occur_dict[item] = 1
    return occur_dict


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Organizes the words through letters and orders them."""
    word_dict: dict[str, list[str]] = {}
    for word in words:
        initial = word[0].lower()
        if initial not in word_dict:
            word_dict[initial] = [word]
        else:
            word_dict[initial].append(word)
    return word_dict


def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """Updates the history of attendance with new information."""
    if day in attendance:
        if student not in attendance[day]:
            attendance[day].append(student)
    else:
        attendance[day] = [student]
    return attendance