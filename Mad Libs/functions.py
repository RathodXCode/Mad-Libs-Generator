import easygui_qt as easy
import random
import os

def twinkle_mad_lib(noun=None, adjective=None, verb=None, adverb=None, place=None):
    if noun is None:
        noun = get_input("Noun:")
        while noun is None or noun == "":
            easy.show_message("You cannot proceed. First, you need to type any word")
            noun = get_input("Noun:")
    if adjective is None:
        adjective = get_input("Adjective:")
        while adjective is None or adjective == "":
            easy.show_message("You cannot proceed. First, you need to type any word")
            adjective = get_input("Adjective:")
    if verb is None:
        verb = get_input("Verb:")
        while verb is None or verb == "":
            easy.show_message("You cannot proceed. First, you need to type any word")
            verb = get_input("Verb:")
    if adverb is None:
        adverb = get_input("Adverb:")
        while adverb is None or adverb == "":
            easy.show_message("You cannot proceed. First, you need to type any word")
            adverb = get_input("Adverb:")
    if place is None:
        place = get_input("Place:")
        while place is None or place == "":
            easy.show_message("You cannot proceed. First, you need to type any word")
            place = get_input("Place:")
    
    result = (
        "Twinkle, twinkle, little {},\n"
        "How I {} what you are.\n"
        "Up above the {} so {},\n"
        "Like a diamond {} in the sky.\n"
        "Twinkle, twinkle, little {},\n"
        "How I {} what you are."
    ).format(noun, verb, place, adjective, adverb, noun, verb)
    easy.show_message(result)
    return_to_menu()

def random_mad_lib(noun=None, verb=None, place=None):
    if noun is None:
        noun = get_input("Noun:")
        while noun is None or noun == "":
            easy.show_message("You cannot proceed. First, you need to type any word")
            noun = get_input("Noun:")
    if verb is None:
        verb = get_input("Verb:")
        while verb is None or verb == "":
            easy.show_message("You cannot proceed. First, you need to type any word")
            verb = get_input("Verb:")
    if place is None:
        place = get_input("Place:")
        while place is None or place == "":
            easy.show_message("You cannot proceed. First, you need to type any word")
            place = get_input("Place:")
    
    result = "The {} likes to {} at the {}.".format(noun, verb, place)
    easy.show_message(result)
    return_to_menu()

def get_input(prompt):
    word = easy.get_string(prompt)
    return word

def get_random_word():
    words = ["cat", "dog", "house", "tree", "sky", "sun", "moon", "star", "car", "computer"]
    return random.choice(words)

def pre_selected(type):
    words = ["cat", "dog", "house", "tree", "sky", "sun", "moon", "star", "car", "computer", "happy", "sad", "big", "small", "red", "blue", "green", "yellow", "fast", "slow"]
    random_words = random.sample(words, 5)
    noun = random_words[0].upper()
    adjective = random_words[1].upper()
    verb = random_words[2].upper()
    adverb = random_words[3].upper()
    place = random_words[4].upper()
    if type == "twinkle":
        result = (
            "Twinkle, twinkle, little <b>{}</b>,\n"
            "How I <b>{}</b> what you are.\n"
            "Up above the <b>{}</b> so <b>{}</b>,\n"
            "Like a diamond <b>{}</b> in the sky.\n"
            "Twinkle, twinkle, little <b>{}</b>,\n"
            "How I <b>{}</b> what you are."
        ).format(noun, verb, place, adjective, adverb, noun, verb)
    elif type == "random":
        result = "The <b>{}</b> likes to <b>{}</b> at the <b>{}</b>.".format(noun, verb, place)
    
    easy.show_message(result)
    return_to_menu()

def return_to_menu():
    if easy.get_choice("Would you like to return to the menu?", choices=["Yes", "No"]) == "Yes":
        os.system("python main.py --skip-welcome")
    else:
        easy.show_message("Goodbye!")
        os._exit(0)