# This is a script to perform a MCQ Testing area for python basics
# Learn Python with Python

# Imports
from os.path import exists
from os import system
from os import get_terminal_size as gts
from time import sleep
from random import shuffle

class Main:
        """Class which is responsible for managing the entire program

        Attr:
            topics: list
            running: bool

        Methods:
            start()
                contains the main loop of the program
        """

        def __init__(self):
            self.topics = ['Basics', 'Control Flow', "Functions", "Lists"]
            self.running = True

        def start(self):
            """Contains the main loop of the program"""
            print("Welcome to Teaching With Python")

            while self.running:
                    print("Insert menu here")
                    self.running = False
            
if __name__ == '__main__':
        main = Main()
        main.start()
