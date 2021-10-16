class Parachute:
    """A code template for our parachute. The responsibility of this class of objects is to update the state of the parachute
     and check if the maximum number of attempts to guess the secret word has been reached.

    Stereotype:
        Information Holder

    Attributes:
        num_wrong_guess (integer): A counter of the attempts made.
        parachute_graphics (list): A list containing the parts of the parachute.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Parachute): An instance of Parachute.
        """
        self.num_wrong_guess = 0        
        self.parachute_graphics = ["  ___",
                                   " /___\\",
                                   " \\   /",
                                   "  \\ /",
                                   "   0",
                                   "  /|\\",
                                   "  / \\",
                                   "\n",
                                   "^^^^^^^"]        
        
    def parachuter(self):
        """Update the parachute status until the game ends.
        Args: 
            self (Parachute): An instance of Parachute.

        Returns:
            string: A string with the state of the parachute.
        """
        if self.num_wrong_guess is not 4:
            skip = "\n".join(self.parachute_graphics[self.num_wrong_guess:])
            return skip
        
        end = "   X\n" + "\n".join(self.parachute_graphics[self.num_wrong_guess + 1:])
        return end
    
    def end(self):
        """Determine if the player has reached the maximum number of attempts.
        Args: 
            self (Parachute): An instance of Parachute.

        Returns:
            booleans: Returns a Boolean value that identifies whether the player has reached the maximum number of attempts.
        """
        max_guess = self.num_wrong_guess >= 4
        return max_guess
    
    def guessed_wrong(self):
        """Every time the player has an error, it is added to the num_wrong_guess.
        Args: 
            self (Parachute): An instance of Parachute.
        """
        self.num_wrong_guess = self.num_wrong_guess + 1
