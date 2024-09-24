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

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

num_wrong_answers = 0

def update_secret_word(random_word, secret_word_list, letter):
    for i in range(len(random_word)):
        if random_word[i] == letter:
            secret_word_list[i] = letter
    return ''.join(secret_word_list)



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
category_dict = {}
for key in game_words.keys():
    print(str(i) + "." + " " + key)
    category_dict[str(i)] = key
    i += 1

    
print('\n')


#Prompt player to choose a category
category_selection = input('Enter the number of your category choice: ')
while category_selection not in category_dict:
    category_selection = input('Oops! Please enter a number from 1 - 10: ')
    
print('\n')

#Tell the player their category
print('Your category is: ' + category_dict[category_selection] + "!")

#Pick a random word from that category and print "_" for each letter in the word
print('Here is your SECRET word...\n')
random_word = game_words[category_dict[category_selection]][random.randint(0,4)].lower()



secret_word_list = []
for letter in random_word:
    secret_word_list.append("_ ")

secret_word_string = ''.join(secret_word_list)

print(secret_word_string)
game_art.hangman(num_wrong_answers) 


print('\n')



while (secret_word_list != list(random_word)) and (num_wrong_answers != 6):
    #Prompt user to guess a letter
    guessed_letter = input('Please guess a letter: ').lower()
    while guessed_letter not in alphabet:
        guessed_letter = input('Oops! Please guess a letter: ').lower()


    #Count how many of the guessed letters are in the chosen word
    #if there aren't any, let the player know
    num_of_times_letter_occurs = random_word.count(guessed_letter)



        
    if guessed_letter in random_word:
        if num_of_times_letter_occurs == 1:
            print('Yes! There is {} {} in the word.\n'.format(num_of_times_letter_occurs, guessed_letter.upper()))
            print(update_secret_word(random_word, secret_word_list, guessed_letter))
            game_art.hangman(num_wrong_answers)   
        else:
            print('Yes! There are {} {}\'s in the word.\n'.format(num_of_times_letter_occurs, guessed_letter.upper()))
            print(update_secret_word(random_word, secret_word_list, guessed_letter))
            game_art.hangman(num_wrong_answers)   
    else:
        print('Nope! There aren\'t any {}\'s is the word.\n'.format(guessed_letter.upper()))
        num_wrong_answers += 1
        game_art.hangman(num_wrong_answers)
        


if num_wrong_answers == 6:
    print('SORRY YOU LOST :(')
else:
    print('WINNER WINNER CHICKEN DINNER!')
    print('The word was {}. Congratulations! You nailed it!'.format(random_word.upper()))