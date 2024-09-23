import game_art
import random


#List of words for the game organized in categories
game_words = {
    'Animals': ['tiger', 'elephant', 'kangaroo', 'giraffe', 'dolphin'],
    'Countries': ['Brazil', 'Canada', 'Austrailia', 'Germany', 'India'],
    'Fruits': ['banana', 'strawberry', 'pineapple', 'watermelon', 'blueberry'],
    'Sports': ['soccer', 'basketball', 'tennis', 'baseball', 'cricket'],
    'Movies': ['Inception', 'Titantic', 'Gladiator', 'Avatar', 'Interstellar'],
    'Famous People': ['Einstein', 'Shakespeare', 'Beethoven', 'Tesla', 'Gandhi'],
    'Foods': ['pizza', 'spaghetti', 'sushi', 'hamburger', 'tacos'],
    'Cities': ['Paris', 'Tokyo', 'New York', 'Sydney', 'London'],
    'Colors': ['red', 'purple', 'turquoise', 'magenta', 'lavender'],
    'Vehicles': ['airplane', 'motorcyle', 'bicycle', 'helicopter', 'submarine']
}


#Print game Intro
print("""
###############################################
#                                             #
#     WELCOME TO THE GAME OF HANGMAN!         #
#                                             #
###############################################

Get ready to test your word-guessing skills in this classic game of Hangman!

RULES:
- You must guess the hidden word one letter at a time.
- Every wrong guess brings the poor stick figure closer to being "hanged!"
- You have 6 chances before the game is over, so choose wisely!

But wait! There's a twist...
You get to choose a CATEGORY to help guide your guesses.

Please select a category to begin:
      """)



#List all categories
i = 1
for key in game_words.keys():
    print(str(i) + "." + " " + key)
    i += 1
    
    
print('\n')
#Prompt player to chose a category
category_selection = int(input('Enter the number of your category choice: '))
while category_selection not in range(1,10):
    category_selection = int(input('Enter the number of your category choice: '))