class Guesser:
    """A code template for our guesser. The responsibility of this class of objects is to verify that the inputs given by
    the guesser are valid. 
    """
    def get_user_guess(self, prompt):
        """Check if the input given by the user is just a letter. If it is a different value, a loop will hold it until
        a valid value is chosen.
        
        Args:
            self (Guesser): An instance of Guesser.
            prompt: User input.         
        """
        while True:
            user_letter = input(prompt)
            
            if user_letter.isalpha() and len(user_letter) == 1:
                return user_letter.lower()
            
            print("Please enter a single letter only.")