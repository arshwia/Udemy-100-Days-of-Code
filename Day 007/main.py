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

print(""" _
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/""")


# functions
def choose_word(words):
    """Choose a random word from a list."""
    random_word = random.choice(words)

    return random_word


def create_hidden_word():
    """Random word selection and word hiding"""
    word = choose_word(words)
    word_length = len(word)

    hidden_word = []
    for _ in range(word_length):
        hidden_word.append("_")

    word_and_hidden_word = [word, hidden_word]

    return word_and_hidden_word


lives = 6


def play_game(lives):
    word, hidden_word = create_hidden_word()
    print(f"Word to guess: {' '.join(hidden_word)}")

    guessed_letters = []

    while lives > 0 and "_" in hidden_word:
        user_letter = input("Guess a letter: ").lower()

        if user_letter in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(user_letter)

        found = False

        for index, letter in enumerate(word):
            if user_letter == letter:
                hidden_word[index] = letter
                found = True

        if not found:
            lives -= 1
            print(f"Wrong! Lives left: {lives}")

        print(f"word to guess: {' '.join(hidden_word)}")

    if "_" not in hidden_word:
        print(f"win\n\tThe word was: {word}")
    else:
        print(f"lose\n\tThe word was: {word}")


play_game(lives)
