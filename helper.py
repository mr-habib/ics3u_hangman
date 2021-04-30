# Habib, Mr
# April 28, 2021
# A helper library for creating a game of Hangman

import random

def display_hangman(num_failed_guesses):
  """Displays a hangman ASCII doodle.

  Displays a hangman ASCII doodle. This was taken from: https://github.com/kiteco/python-youtube-code/blob/master/build-hangman-in-python/hangman.py#L60

  Args:
    num_failed_guesses: The number of times a user has failed a guess.

  Returns:
    None

  Side Effects:
    Prints the doodle.
  """

  stages = [  # final state: head, torso, both arms, and both legs
            """
                --------
                |      |
                |      O
                |     \\|/
                |      |
                |     / \\
                -
            """,
            # head, torso, both arms, and one leg
            """
                --------
                |      |
                |      O
                |     \\|/
                |      |
                |     / 
                -
            """,
            # head, torso, and both arms
            """
                --------
                |      |
                |      O
                |     \\|/
                |      |
                |      
                -
            """,
            # head, torso, and one arm
            """
                --------
                |      |
                |      O
                |     \\|
                |      |
                |     
                -
            """,
            # head and torso
            """
                --------
                |      |
                |      O
                |      |
                |      |
                |     
                -
            """,
            # head
            """
                --------
                |      |
                |      O
                |    
                |      
                |     
                -
            """,
            # initial empty state
            """
                --------
                |      |
                |      
                |    
                |      
                |     
                -
            """
  ]
  print(stages[num_failed_guesses])

def get_word():
  with open('wordlist.txt') as file_in:
    return random.choice(file_in.readlines()).strip()