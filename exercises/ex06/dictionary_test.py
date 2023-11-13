"""EX07: `dict` Unit Tests."""
__author__ = "730577037"


from exercises.ex06.dictionary import invert, count, favorite_color, alphabetizer, update_attendance


def test_invert_empty() -> None:
    """Tests when the dictionary is empty."""
    dictionary: dict[str, str] = {}
    assert invert(dictionary) == {} 


def test_invert_normal_single() -> None:
    """Tests when the dictionary has one pair."""
    dictionary: dict[str, str] = {"Enis": "Sevim"}
    assert invert(dictionary) == {"Sevim": "Enis"}


def test_invert_normal_double() -> None:
    """Tests when the dictionary has two pairs."""
    dictionary: dict[str, str] = {"Enis": "Sevim", "Apple": "Pineapple"}
    assert invert(dictionary) == {"Sevim": "Enis", "Pineapple": "Apple"}


def test_favorite_color_empty() -> None:
    """Tests when the dictionary has no colors."""
    dictionary: dict[str, str] = {}
    assert favorite_color(dictionary) == ""


def test_favorite_color_one() -> None:
    """Tests when the dictionary has one color that is the most frequent."""
    dictionary: dict[str, str] = {"Enis": "Blue", "Josh": "Blue", "Bob": "Red"}
    assert favorite_color(dictionary) == "Blue"


def test_favorite_color_tie() -> None:
    """Tests when the dictionary has a tie between colors."""
    dictionary: dict[str, str] = {"Enis": "Blue", "Josh": "Blue", "Bob": "Red", "George": "Red"}
    assert favorite_color(dictionary) in ["Blue", "Red"]


def test_count_empty() -> None:
    """Tests when the dictionary is empty."""
    dictionary: list[str] = []
    assert count(dictionary) == {}


def test_count_multiple() -> None:
    """Tests when the dictionary has multiple different items."""
    dictionary: list[str] = ["Enis", "Josh", "Bob", "George", "Enis"]
    assert count(dictionary) == {"Enis": 2, "Josh": 1, "Bob": 1, "George": 1}


def test_count_same() -> None:
    """Tests when the dictionary has all the same items."""
    dictionary: list[str] = ["Enis", "Enis", "Enis"]
    assert count(dictionary) == {"Enis": 3}


def test_alphabetizer_empty() -> None:
    """Tests when the dictionary is empty."""
    dictionary: list[str] = []
    assert alphabetizer(dictionary) == {}


def test_alphabetizer_one() -> None:
    """Tests when the dictionary has one word."""
    dictionary: list[str] = ["Enis"]
    assert alphabetizer(dictionary) == {"e": ["Enis"]}


def test_alphabetizer_multiple() -> None:
    """Tests when the dictionary has multiple words."""
    dictionary: list[str] = ["Enis", "Bob", "Joe", "Bill"]
    assert alphabetizer(dictionary) == {"b": ["Bob", "Bill"],
                                        "e": ["Enis"],
                                        "j": ["Joe"]}


def test_attendance_empty() -> None:
    """Tests when the dictionary is empty."""
    dictionary: dict[str, list[str]] = {}
    day: str = "Monday"
    student: str = "Enis"
    assert update_attendance(dictionary, day, student) == {"Monday": ["Enis"]}


def test_attendance_new() -> None:
    """Tests when the day does not exist in the dictionary."""
    dictionary: dict[str, list[str]] = {"Monday": ["Enis", "Bob"]}
    updated = update_attendance(dictionary, "Tuesday", "Bob")
    assert updated == {"Monday": ["Enis", "Bob"], "Tuesday": ["Bob"]}


def test_attendance_exist() -> None:
    """Tests when the day already exists in the dictionary."""
    dictionary: dict[str, list[str]] = {"Monday": ["Enis", "Bob"]}
    updated = update_attendance(dictionary, "Monday", "Joe")
    assert updated == {"Monday": ["Enis", "Bob", "Joe"]}