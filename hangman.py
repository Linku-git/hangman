import random

# List of words to choose from
words = [
    "python", "programming", "computer", "science", "algorithm",
    "database", "network", "security", "software", "developer",
    "interface", "javascript", "machine", "learning", "artificial",
    "intelligence", "framework", "library", "function", "variable",
    "object", "class", "inheritance", "polymorphism", "encapsulation",
    "debugging", "testing", "version", "control", "repository"]

# ASCII art for hangman stages
hangman_art = [
    """
       ____
      |    |
      |
      |
      |
      |
    __|__
    """,
    """
       ____
      |    |
      |    O
      |
      |
      |
    __|__
    """,
    """
       ____
      |    |
      |    O
      |    |
      |
      |
    __|__
    """,
    """
       ____
      |    |
      |    O
      |   /|
      |
      |
    __|__
    """,
    """
       ____
      |    |
      |    O
      |   /|\\
      |
      |
    __|__
    """,
    """
       ____
      |    |
      |    O
      |   /|\\
      |   /
      |
    __|__
    """,
    """
       ____
      |    |
      |    O
      |   /|\\
      |   / \\
      |
    __|__
    """
]

def choose_word():
    return random.choice(words)

def play_hangman():
    word = choose_word()
    word_letters = set(word)
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    used_letters = set()

    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print("\nYou have", lives, "lives left.")
        print("Used letters:", ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '_' for letter in word]
        print("Current word:", ' '.join(word_list))

        print(hangman_art[6 - lives])

        user_letter = input("Guess a letter: ").lower()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print("Letter is not in the word.")
        elif user_letter in used_letters:
            print("You have already used that letter. Please try again.")
        else:
            print("Invalid character. Please try again.")

    if lives == 0:
        print(hangman_art[6])
        print("Sorry, you died. The word was", word)
    else:
        print("Congratulations! You guessed the word", word, "!!")

while True:
    play_hangman()
    if input("Play Again? (Y/N) ").lower() != 'y':
        break