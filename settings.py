import datetime
class Settings:
    def __init__(self):
        self.started=datetime.datetime.now()
        self.number_of_guesses = 10
        self.mode = "EASY"
        self.code_length = 4
        self.numbers_of_colours = 8