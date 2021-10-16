import random
import re
import os
from csv import reader 

class Word:
    """A code template for our word. The responsibility of this class of objects is to choose the secret word and verify
    that the user can guess it.
    
    Stereotype:
        Information Holder

    Attributes:
        letter_guessed (list): A list containing the letters entered by the user.
        words (list): A list of words from which the program will randomly choose one for the game.
        chosen_word (string): The secret word.
        blank_word (list): A list containing the number of blanks referring to the secret word.
    """

    def __init__(self):
        """The class constructor.
        Args:
            self (Word): An instance of Word.
        """
        self.letter_guessed = ["_"]
        self.words = self.wordsrandom()
        self.chosen_word = self.random_word() 
        print(self.chosen_word)       
        self.blank_word = ["_"] * len(self.chosen_word)
    
    def wordsrandom(self):
        path = os.path.dirname(os.path.realpath(__file__))
        with open(f"{path}\\randomwords.csv", mode="r") as file:
            reader_file = reader(file)
            list_of_words = list(reader_file)
            return list_of_words

    def secret_word(self):
        """Determine the number of blanks it must have to represent the letters of the secret word.
        Args:
            self (Word): an instance of Word.
        
        Returns:
            string: returns a string with the number of blanks that refer to the letters of the secret word.

        """
        for i in re.finditer(self.letter_guessed[-1], self.chosen_word):
            index = i.start()
            self.blank_word[index] = self.letter_guessed[-1]
        
        blank_word = " ".join(self.blank_word)
        return blank_word
    
   
    def see_blank(self):
        """Check if blank_world has blank spaces.
        Args:
            self (Word): An instance of Word.
        Returns:
            booleans: Check if blank_world has blank spaces.
        """
        if ["_"] is not self.blank_word:
            return False
        else:
            return True
    
   
    def verify_letter(self, user_guess):
        """Verify and add the letters entered by the user.
        Args:
            self (Word): An instance of Word.
            user_guess: User input.
        Returns:
            string: Add the letters entered by the user
        """
        if user_guess not in self.letter_guessed:
            return self.letter_guessed.append(user_guess)
        else:
            return False
    
    
    def letter_in_list(self, user_guess):
        """Check if the letter entered by the user is part of the secret word.
        Args:
            self (Word): An instance of Word.
            user_guess: User input.
        Returns:
            booleans: Check if the letter entered by the user is part of the secret word.
        """
        return user_guess in self.chosen_word
    
    
    def random_word(self):
        """Pick a random word from a list.
        Args:
            self (Word): An instance of Word.
        
        Returns:
           String: A word is chosen at random
        """
        self.chosen_word = random.choice(self.words)
        print(self.chosen_word)
        return self.chosen_word