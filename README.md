# HANGMAN (word guessing game)
---
#### Description:
This is a word guessing game in python. The user runs the program and tries to guess the word before the chances run out. I used pyfilget to print in a cool font the welcome and exit messages when running the program. I also used the Colors Class in order to print different colors to the terminal cyan, red, and yellow to make it easier to read. I made this decision in order to make the program more exciting and avoid the bland nature of the terminal. A welcome screen and a disclaimer is shown to the user in the beginning og the programm. The categories for the words are also shown to the user. The user must first choose a category. The user is then prompted for a number of the category. Once entered, it is validated if its one of the valid options. Once a category is chosen a random word in that category is chosen and the user must try to guess that word. A load words function is called to get the words list for that category, the words are read and random.choice chooses one word in those words. The game is able to select the word depending on the category. The words folder contains 3 .txt files that contain words for each category (cars, sports and countries). If the user at any point types "exit" or "quit", they will exit the application. One or more letters of the chosen word are shown to the user in order to give them a hint. If the word contains spaces they are automatically filled in and shown as part of the hint (the user does not need to guess them). The chances are equal to the word length. The user is then continuosly prompted for a letter in the chosen word The chances decrease every time the user guesses an incorrect guess and a corresponding response in red is shown. The chances do not decrease if the user guesses a letter that has already been guesses and they are shown a message in yellow. If the user enters full words / invalid characters instead of single letters they are given an indication to enter a single letter and shown the message in yellow. The sickman folder contains a .txt file that has drawings of the different chance levels of stickman. The stickman figures are drawn when the user makes a wrong a guess and has 5 or below than 5 guesses left. A drawing corresponding to the chance level is drawn. Upon making the guess it is checked whether it is a an exit prompt, a single letter and if its a valid character or an invalid character. It is then checked if it is one of the missing letters (correct guess) or not. The update user guess function is called on a correct guess and the user's progress word is updated with the guess. The user loses when they run out of guesses and then the correct word is shown. The user wins if they guess the word before running out of chances, then the program will exit.
#### Running the program:
    Exacute "python3 project.py" in terminal

#### Testing th program:
    Execute "pytest test_project.py" in terminal

