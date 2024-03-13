import random
import pyfiglet


class Colors:
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'


def update_user_guess(word, user_word_progress, user_letter_guess):
    updated_word = ""
    for index, letter in enumerate(word):
        if letter == user_letter_guess:
            updated_word += user_letter_guess
        else:
            updated_word += user_word_progress[index]
    
    return updated_word


def get_missing_letters(correct_word, user_word_progress):
    missing_letters = ""
    for index, letter in enumerate(correct_word):
        if letter == user_word_progress[index]:
            missing_letters += ""
        else:
            missing_letters += letter

    return missing_letters


def load_words_chosen_category(category):
    category = category.lower()

    if category == "cars" or category == "car":
        path = "cars"

    elif category == "sport" or category == "sports":
        path = "sports"

    if category == "country" or category == "countries":
        path = "countries"

    try:
        with open(f"words/{path}.txt", 'r') as file:
            words = file.read().strip().split('\n')
            return words
    except FileNotFoundError:
        text = f"Words not found for category: {path}, exiting application"
        print_with_color(text, "red")
        exit()


def show_disclaimer():
    return "You can exit this application by typing 'exit' or 'quit'\n"


def show_categories():
    return """These are the available categories for the hangman words: 
1. Cars
2. Sports
3. Countries
"""


def get_user_category():
    categories = {"1": "cars",
                  "2": "sports",
                  "3": "countries",}
    while True:
        number = input("Enter category (e.g 1.): ")

        if number.lower() in categories.keys():
            category = categories[number]
            return category, f"\nYou chose the '{category}' category for this hangman game"
            
        elif number.lower() == "exit" or number.lower() == "quit":
            return None, None

        else:
            text = "Invalid category number, try again\n"
            print_with_color(text, "red")
            continue


def show_goodbye():
    return pyfiglet.figlet_format("\nGOODBYE, THANKS FOR PLAYING", font = "mini" ) 


def start_program():
    return pyfiglet.figlet_format("WELCOME  TO  HANGMAN", font = "mini" ) 
    


def print_with_color(text, color):
    if color == "red":
        print(Colors.RED + text + Colors.CYAN)
    elif color == "green":
        print(Colors.GREEN + text + Colors.CYAN)
    elif color == "yellow":
        print(Colors.YELLOW + text + Colors.CYAN)
    elif color == "blue":
        print(Colors.BLUE + text + Colors.CYAN)
    elif color == "purple":
        print(Colors.PURPLE + text + Colors.CYAN)
    elif color == "cyan":
        print(Colors.CYAN + text + Colors.CYAN)



def load_stickman():
    try:
        with open("stickman/stickman5.txt", 'r') as file:
            drawings = file.read().strip().split('\n\n')
    except FileNotFoundError:
        text = "Stickman drawings not found, exiting application"
        print_with_color(text, "red")
        exit()
    
    return drawings


def main():
    print(Colors.CYAN)
    print(start_program())
    print(show_disclaimer())
    print(show_categories())
    
    category, text = get_user_category()
    if category:
        print(text)
        words = load_words_chosen_category(category)
    else:
        print(show_goodbye())
        exit()
    
    word = random.choice(words)
    chances = len(word)

    user_word_progress = "-"*len(word)
    already_guessed_letters = " "
    drawings = load_stickman()
    guesses = 0
    
    # replace spaces
    if " " in word:
        user_word_progress = update_user_guess(word, user_word_progress, " ")
    
    # show letter(s) at start
    while True:
        random_letter = random.choice(word)
        if random_letter in already_guessed_letters:
            continue
        else:
            already_guessed_letters += random_letter
            user_word_progress = update_user_guess(word, user_word_progress, random_letter)
            break

    while True:  
        # display underscores
        print("\n\n")
        print(f"Try to guess the {category} name: {user_word_progress}")
        print(f"You have {chances} chances left")

        # take a guess (prompt)
        user_letter_guess = input(f"\nType a letter: ")

        # exit
        missing_letters = get_missing_letters(word, user_word_progress)
        if user_letter_guess.lower() == "quit" or user_letter_guess.lower() == "exit":
            print(show_goodbye())
            exit()

        # user types a word instead of letter
        elif len(user_letter_guess) > 1 or not user_letter_guess.isalpha():
            text  = "Type a single letter/alphabet"
            print_with_color(text, "yellow")
            continue

        # if right
        elif user_letter_guess.lower() in missing_letters:
            user_word_progress = update_user_guess(word, user_word_progress, user_letter_guess.lower())
            text = "You made a correct guess"
            print_with_color(text, "green")
        
        # if already guessed
        elif user_letter_guess in already_guessed_letters:
            text = "you have already guessed this character, try again"
            print_with_color(text, "yellow")

        # if wrong
        else:
            text = f"you made a wrong guess"
            print_with_color(text, "red")
            
            if chances <= 5:
                text = drawings[-chances]
                print_with_color(text, "red")

            chances -= 1

        already_guessed_letters += user_letter_guess
        guesses += 1

        # check if whole word guessed yet
        if word == user_word_progress:
            text = f"You won!, you guessed the word in {guesses} guesses"
            print_with_color(text, "green")
            text = f"\nThe word was, '{word}'"
            print_with_color(text, "green")
            print(show_goodbye())
            exit()
        
        # out of chances
        if word != user_word_progress and chances == 0:
            text = f"\nYou have {chances} chances left"
            print_with_color(text, "red")
            text = f"\nThe word was, '{word}'"
            print_with_color(text, "green")
            print(show_goodbye())
            exit()



if __name__ == "__main__":
    main()