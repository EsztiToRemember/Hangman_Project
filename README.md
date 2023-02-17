# Hangman_Project
Hangman Game;

This is a simple implementation of the Hangman game in Python.

How to Play

When you run the game, a word will be chosen at random and the player will be prompted to guess letters until they can guess the entire word, or until they run out of guesses.
The player can guess a letter by typing it into the console. If the letter is part of the word, it will be revealed in the correct position(s). If the letter is not part of the word, the player will lose one of their guesses.
If the player guesses all the letters before running out of guesses, they win the game. If they run out of guesses before guessing all the letters, they lose the game.

Game Settings

The game settings can be adjusted at the top of the hangman.py file:

'tries': the maximum number of guesses the player has

'words': the list of words to choose from


Hints

The player can choose to receive a hint for the word by typing "y" when prompted if they want a hint. The hint will be a letter from the word that the player has not yet guessed.
Hints will be available on the last 4 tries if the player got a letter wrong. 
You can adjust the number of hints in 'if tries in [4, 3, 2, 1] and letter not in word:'


Credits

This project was created by Eszter Parnicsan and is based on the idea of the classic game of Hangman.
