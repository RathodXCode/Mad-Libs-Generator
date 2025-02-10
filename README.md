# Mad Libs Generator

## Project Overview
This project is a Mad Libs Generator developed by Neil Rathod for the CS 20 course. It allows users to create fun and random stories by filling in the blanks with different types of words.

## Features
- **Input-Based Mad Libs**: Users can input their own words to generate a Mad Lib.
- **Pre-selected Mad Libs**: The program can randomly select words to generate a Mad Lib.

## Requirements
- Python 3.12.2
- `easygui_qt` library
- `OS` library
- `sys` library

## Installation
1. Clone the repository or download the source code.
2. Install the required library using pip:
    ```bash
    pip install easygui_qt
    pip install os
    pip install sys
    ```

## Usage
1. Run the `main.py` script to start the Mad Libs Generator:
    ```bash
    python main.py
    ```
2. Follow the on-screen prompts to create your Mad Lib.

## File Descriptions
- **main.py**: The main script that starts the program and displays the menu.
- **functions.py**: Contains the functions for generating Mad Libs and handling user input.

## Functions
### main.py
- **twinkle_mad_lib**: Generates a "Twinkle, Twinkle, Little Star" themed Mad Lib based on user input.
- **pre_selected**: Generates a Mad Lib using randomly selected words.

### functions.py
- **twinkle_mad_lib**: Prompts the user for various types of words and generates a "Twinkle, Twinkle, Little Star" themed Mad Lib.
- **random_mad_lib**: Prompts the user for a noun, verb, and place to generate a random Mad Lib.
- **get_input**: Helper function to get user input using a GUI prompt.
- **get_random_word**: Returns a random word from a predefined list.
- **pre_selected**: Generates a Mad Lib using randomly selected words.
- **return_to_menu**: Asks the user if they want to return to the menu or exit the program.

## Author
Neil Rathod
