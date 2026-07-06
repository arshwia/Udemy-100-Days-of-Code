import random

# data
words = [
    "apple",
    "banana",
    "orange",
    "grape",
    "mango",
    "lemon",
    "peach",
    "cherry",
    "strawberry",
    "watermelon",
    "python",
    "computer",
    "keyboard",
    "monitor",
    "mouse",
    "window",
    "coffee",
    "school",
    "teacher",
    "student",
    "library",
    "elephant",
    "tiger",
    "lion",
    "rabbit",
    "monkey",
    "penguin",
    "guitar",
    "camera",
    "planet",
]


# functions
def choose_word(words):
    """Choose a random word from a list."""
    random_word = random.choice(words)

    return random_word


def hidden_word_def():
    word = choose_word(words)
    word_length = len(word)

    hidden_word = ""
    for _ in range(word_length):
        hidden_word += "_ "

    print(word)
    print(hidden_word)
    return hidden_word


def play_game():
    hidden_word = hidden_word_def()


def display_hangman():
    print()


play_game()
