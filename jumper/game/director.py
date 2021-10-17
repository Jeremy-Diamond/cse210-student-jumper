from game.guesser import Guesser
from game.word import Word
from game.parachute import Parachute


class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to keep track of the score and control the 
    sequence of play.
    
    Attributes:
        keep_playing (boolean): Whether or not the player wants to keep playing.
        parachute: Will take care of the graphics.
        guesser: User guesses the secret word by imputing a letter.
        word: Will take of getting a random word and respond to user inputs.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.word = Word()
        self.parachute = Parachute()
        self.guesser = Guesser()        
        self.keep_playing = True        

    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): An instance of Director.
        """
        self.do_outputs()
        
        while self.keep_playing:
            self.get_inputs()
            self.do_outputs()

    def do_outputs(self):
        """ Outputs the important game information for each round of play. In this case, as the game progresses, the state of the parachute
        changes, and the letters that the player correctly guessed appear.

        Args: self(Director): An instance of Director.
        """
        print(self.word.secret_word())  
        print()
        print(self.parachute.parachuter())
        
        
        self.keep_playing = not self.parachute.end() or self.word.see_blank() or self.word.win_game()
        
        if self.keep_playing is False:
            if "_" not in self.word.blank_word:
                print("Congratulations, you have won!")

            else: 
                print("Sorry your parachuter has fallen and you have lost the game.")
            exit
            

    def get_inputs(self):
        """ Gets the inputs at the beginning of each round of play. In this case, it gets the letters added by the user and verifies that they
        are part of the secret word.

        Args: self(Director): An instance of Director.
        """
        user_guess = self.guesser.get_user_guess("Guess a letter [a-z]: ")
        
        while self.word.verify_letter(user_guess) == False:
            print("Please enter a different letter.")
            user_guess = self.guesser.get_user_guess("Guess a letter [a-z]: ")
        
        if self.word.letter_in_list(user_guess) == False:
            self.parachute.guessed_wrong()