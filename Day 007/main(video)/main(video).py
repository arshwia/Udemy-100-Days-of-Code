import random
import hangman_words
import hangman_stages

lives = 6

choice_word = random.choice(hangman_words.word_list)
print(choice_word)

placeholder = ""
for position in range(1, len(choice_word)):
    placeholder += "_"
print(placeholder, len(placeholder))

game_over = False
correct_letter = []

while not game_over:
    guess = input("Guess a letter: ").lower()

    if guess in correct_letter:
        print(f"You've already guessed: {guess}")

    display = ""
    for letter in choice_word:
        if letter == guess:
            display += letter
            correct_letter.append(guess)
        elif letter in correct_letter:
            display += letter
        else:
            display += "_"

    print(display)

    if guess not in choice_word:
        lives -= 1
        if lives == 0:
            print("loseeeeeeeeeeeeee")
            break

    if "_" not in display:
        game_over = True
        print("winnnnnnnnnnnnnnn")

    if lives < len(hangman_stages.stages):
        print(hangman_stages.stages[lives])
