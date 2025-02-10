#############################################################################
#NAME OF THE PROJECT: Mad Libs Generator
#DEVLOPER: Neil Rathod
#COURSE: CS 20
#############################################################################

import easygui_qt as easy #for GUI
import os #to exit the program
import sys #to skip the welcome message

#Importing FUNCTION from functions.py
from functions import twinkle_mad_lib, pre_selected

#wELCOME MESSAGE
skip_welcome = "--skip-welcome" in sys.argv


if not skip_welcome:
    easy.show_message("Welcome to the Mad Libs Generator!")

#OPTIONS
choices = ["Input-Based", "Pre-selected"]

choice = easy.get_choice("Start your mad lib", choices=choices)

#MENU
if choice == "Input-Based":
    twinkle_mad_lib()
elif choice == "Pre-selected":
    pre_selected("twinkle")
else:
    easy.show_message("Goodbye!")
    os._exit(0)