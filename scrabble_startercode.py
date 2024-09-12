'''
SCRABBLE TEST STARTER CODE
Coder: [your name here]
Date: [date here]

It's always good practice to leave a comment at the top of a big project.
This way if you want to look back at this project in a few years, you can see when you wrote it
and what it does.

Write a brief description of this project here.

'''

'''
If your project needs any modules (it does), your import statements should go here
'''

# Here are some data structures you will need for the project. They are GLOBAL variables
import random as r
# TILES contains all the same tiles as a scrabble bag, with the same quantities too
TILES = ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'A', 'I', 'A', 'I', 'A', 'I', 'A', 'I', 'A',
         'I', 'A', 'I', 'A', 'I', 'A', 'I', 'A', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'N', 'R', 'T', 'N',
         'R', 'T', 'N', 'R', 'T', 'N', 'R', 'T', 'N', 'R', 'T', 'N', 'R', 'T', 'L', 'S', 'U', 'L', 'S', 'U', 'L',
         'S', 'U', 'L', 'S', 'U', 'D', 'D', 'D', 'D', 'G', 'G', 'G', 'B', 'C', 'M', 'P', 'B', 'C', 'M', 'P',
         'F', 'H', 'V', 'W', 'Y', 'F', 'H', 'V', 'W', 'Y', 'K', 'J', 'X', 'Q', 'Z']

# tile_to_points maps a letter to the number of points it is worth when played
tile_to_points = {'E': 1, 'A': 1, 'I': 1, 'O': 1, 'N': 1, 'R': 1, 'T': 1, 'L': 1, 'S': 1, 'U': 1, 'D': 2, 'G': 2,
                  'B': 3, 'C': 3, 'M': 3, 'P': 3, 'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4, 'K': 5, 'J': 8, 'X': 8,
                  'Q': 10, 'Z': 10}

'''
You should have been given a file 'Collins Scrabble Words (2019).txt'.
This file contains all valid scrabble words, in all uppercase, with one per line.
Open the file, read the contents into a list.
Your list 'valid_words' should contain every word from the file, each word being its own element.
Remember a line in a file always ends with a newline character, account for this somehow.
When you are done reading the file, make sure it is closed.
'''

## FUNCTION SPACE ##

# GAME PLAY FUNCTIONS #
# by creating these two input sanitization functions, our later code is much cleaner


def int_input(prompt):
    num = input(prompt)
    while num.isdigit() == False:
        num = input(prompt)
    return int(num)


def str_input(prompt):
    stri = input(prompt)
    while stri.isalpha() == False:
        stri = input(prompt)
    return str(stri)


def get_new_tiles(num):
    hand = r.sample(TILES, num)
    for i in hand:
        TILES.remove(i)
    return hand


def print_hand(hand):
    for tile in hand:
        for key, value in tile_to_points.items():
            if tile == key:
                print(key, ":", value)


def get_points(word):
    total = 0
    for letter in word:
        for key, value in tile_to_points.items():
            if letter == key:
                total += value
    return total


def is_valid_play(word, hand):
    '''
    The parameter 'word' is a word the player is attempting to play, and 'hand' is that player's hand.
    This function needs to return True if this word is a valid play, and False otherwise.
    A word is a valid play if it only uses the tiles from hand AND contains at least one letter.
    It ALSO must be a valid scrabble word, as determined by the valid_words list.

    EX:
    is_valid_play('DOG', ['D', 'G', 'O', 'H', 'A', 'V', 'B']) is True
    is_valid_play('GLUE', ['D', 'G', 'O', 'H', 'A', 'V', 'B']) is False, hand does not have L, U, or E
    is_valid_play('DAD', ['D', 'G', 'O', 'H', 'A', 'V', 'B']) is False, there is only one D in hand
    is_valid_play('', ['D', 'G', 'O', 'H', 'A', 'V', 'B']) is False, word has to have some letters
    is_valid_play('VB', ['D', 'G', 'O', 'H', 'A', 'V', 'B']) is False, VB is not a valid scrabble word
    '''
    pass

# GAME STATISTIC FUNCTIONS #


def get_winner():
    '''
    Does this function need parameters? Up to you.
    This function needs to return the name of the winning player.
    The winning player is the player with the most points.
    '''
    pass


def get_best_word():
    '''
    Does this function need parameters? Up to you.
    This function should return the highest scoring word played.
    '''
    pass

## GAME STARTS ##


'''
There is nothing to be added or changed in this section! Skip down to 
line 190 for your next tasks.
'''

num_players = int_input("Number of players: ")
player_to_words = {}  # maps a player to the words they have played
player_to_points = {}  # maps a player to the poins they have earned
player_to_hand = {}  # maps a player to a list of the tiles in their hand

# initialising all the dictionaries
for i in range(1, num_players + 1):
    name = str_input("Enter name of player " + str(i) + ": ")
    player_to_words[name] = []
    player_to_points[name] = 0
    player_to_hand = get_new_tiles(7)

# MAIN GAME LOOP #
# this section contains the part of the game that repeats until the game is over
# the game is over if they run out of tiles or players choose to stop

choice = ""

while len(TILES) > 0 and choice < 1:
    print("---- NEW ROUND ----")
    for player in player_to_words:
        print("--%s's TURN--" % (player))  # this prints whose turn it is now
        print_hand(player_to_hand[player])  # let them see their hand
        print("Options for your turn:\n0 - \t pick new tiles\n1 - \t play word\nany other number - \t STOP GAME")
        # player enters 0 to replace hand, 1 to play a word, and anything else to quit game
        choice = int_input("Enter a number to select: ")

        if choice == 0:
            # put their tiles back in the pool
            TILES.extend(player_to_hand[player])
            player_to_hand[player] = get_new_tiles(7)  # replace their hand
            print_hand(player_to_hand[player])  # show the new hand
            print("END OF TURN")

        elif choice == 1:
            word = str_input("Enter the word to play: ")
            # they can only play valid words!
            if not is_valid_play(word, player_to_hand[player]):
                print("INVALID GUESS - TURN SKIPPED")
            else:
                player_to_words[player].append(word)  # update word dictionary
                # find out how many points they earned
                points = get_points(word)
                print("Your word earned", points, "points!")
                player_to_points[player] += points  # update points dictionary
                for char in word:
                    # remove tiles from their hand
                    player_to_hand[player].remove(char)
                player_to_hand[player].extend(
                    get_new_tiles(7 - len(word)))  # refill their hand
                print("UPDATED HAND:")
                print_hand(player_to_hand[player])  # show them their new hand

        else:
            print("STOPPING GAME...")
            break  # get out of the for loop, while condition will be checked and will be false

print("GAME OVER - GENERATING GAME STATS")

'''
Print out some relevant stats about the game! You need to give at least
 - the name of the winner and how many points they earned
 - the best scoring word played in the game

(OPTIONAL)
You can print out other stats if you want! For example:
 - the longest word played
 - the best word from each player
 - the number of words played
 - the number of rounds played

'''
