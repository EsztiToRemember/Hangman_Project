import random

# Load the high scores from file
def load_high_scores():
    high_scores = {}
    with open("high_scores.txt.txt", "r") as f:
        for line in f:
            name, score = line.strip().split(":")
            high_scores[name] = int(score)
    return high_scores

# Save the high scores to file
def save_high_scores(high_scores):
    with open("high_scores.txt.txt", "w") as f:
        for name, score in high_scores.items():
            f.write(f"{name}:{score}\n")

# Display the high scores
def display_high_scores():
    high_scores = load_high_scores()
    sorted_scores = sorted(high_scores.items(), key=lambda x: x[1], reverse=True)
    print("High Scores:")
    for name, score in sorted_scores:
        print(f"{name}: {score}")
    print()

def play_hangman():
    words = ["python", "java", "ruby", "javascript", "php", "apple", "banana", "red", "orange", "yellow", "green", "blue", "purple", "pink", "brown", "black", "white", "gray", "silver", "gold", "beige", "cream", "ivory", "olive", "teal", "turquoise", "aqua", "navy", "indigo", "violet", "magenta", "orange", "pear", "grape", "kiwi", "emerald", "forest", "lime", "mint", "sage", "olive", "khaki", "taupe", "charcoal", "ebony", "onyx", "ivory", "watermelon", "pineapple", "lemon", "lime", "peach", "plum", "strawberry", "blueberry", "raspberry", "blackberry", "mango", "papaya", "apricot", "cherry", "fig", "coconut", "avocado", "potato", "carrot", "broccoli", "cauliflower", "cucumber", "lettuce", "spinach", "tomato", "pepper", "onion", "garlic", "chicken", "beef", "pork", "fish", "shrimp", "lobster", "crab", "duck", "turkey", "goose", "egg", "cheese", "yogurt", "butter", "honey", "tiger", "lion", "elephant", "giraffe", "rhinoceros", "hippopotamus", "crocodile", "alligator", "zebra", "monkey", "gorilla", "chimpanzee", "orangutan", "lemur", "koala", "kangaroo", "wallaby", "wombat", "platypus", "kookaburra", "emu", "ostrich", "parrot", "peacock", "eagle", "hawk", "owl", "penguin", "puffin", "seagull", "pelican", "duck", "swan", "flamingo", "crane", "stork", "deer", "moose", "elk", "bear", "wolf", "fox", "coyote", "raccoon", "skunk", "squirrel", "chipmunk", "rabbit", "hedgehog"]
    word = random.choice(words)
    guessed = "_" * len(word)
    tries = 10
    letters_tried = []
    hint_given = False
    high_scores = load_high_scores()
    name = input("Enter your name: ")
    while tries > 0 and guessed != word:
        print("Guess the word:", guessed)
        print("Tries left:", tries)
        if tries in [4, 3, 2, 1] and letter not in word:
            print("Do you want a hint? (y/n)")
            answer = input().lower()
            if answer == "y":
                hint_index = random.randint(0, len(word) - 1)
                while word[hint_index] in letters_tried:
                    hint_index = random.randint(0, len(word) - 1)
                print(f"The letter at index {hint_index+1} is {word[hint_index]}")
                hint_given = True
        letter = input("Enter a letter: ").lower()
        if len(letter) == 1 and letter.isalpha():
            if letter in letters_tried:
                print("You already tried that letter!")
            elif letter in word:
                print("Good job! The letter is in the word.")
                letters_tried.append(letter)
                guessed = "".join([letter if letter == word[i] else guessed[i] for i in range(len(word))])
            else:
                print("Sorry, the letter is not in the word.")
                letters_tried.append(letter)
                tries -= 1
        else:
            print("Please enter a single letter.")
    if tries == 0:
        print("You lost. The word was", word)
    else:
        print("Congratulations, you guessed the word", word, "!")
        score = tries * len(word)
        print(f"You scored {score} points!")
        if name not in high_scores or score > high_scores[name]:
            high_scores[name] = score
            save_high_scores(high_scores)
            print("Congratulations, you set a new high score!")
        display_high_scores()

# Start the Hangman game
play_hangman()