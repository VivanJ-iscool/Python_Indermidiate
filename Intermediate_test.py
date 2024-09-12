import random as r
TILES = ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'A', 'I', 'A', 'I', 'A', 'I', 'A', 'I', 'A', 'I', 'A', 'I', 'A', 'I', 'A', 'I', 'A', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'N', 'R', 'T', 'N', 'R', 'T', 'N', 'R', 'T', 'N', 'R', 'T', 'N', 'R', 'T', 'N', 'R', 'T', 'L', 'S', 'U', 'L', 'S', 'U', 'L', 'S', 'U', 'L', 'S', 'U', 'D', 'D', 'D', 'D', 'G', 'G', 'G', 'B', 'C', 'M', 'P', 'B', 'C', 'M', 'P', 'F', 'H', 'V', 'W', 'Y', 'F', 'H', 'V', 'W', 'Y', 'K', 'J', 'X', 'Q', 'Z']
tile_to_points = {'E': 1, 'A': 1, 'I': 1, 'O': 1, 'N': 1, 'R': 1, 'T': 1, 'L': 1, 'S': 1, 'U': 1, 'D': 2, 'G': 2,'B': 3, 'C': 3, 'M': 3, 'P': 3, 'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4, 'K': 5, 'J': 8, 'X': 8, 'Q': 10, 'Z': 10}


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

#example for 3 and 4
print(len(TILES)) 
h = get_new_tiles(7)
print(h)
print(len(TILES))

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


#6
def is_valid_play(word, hand):
    isvalidplay = False
    for letter in word:
        if letter in hand and len(word) >= 1:
                isvalidplay == True
    return isvalidplay


#7
def get_winner(player_to_points):
    win_point = 0
    for player,points in player_to_points.items():
        if points>win_point:
            win_point = points
            Winner = player

    return Winner
    
    # player1_points = player_to_points[player1]
    # player2_points = player_to_points[player2]
    # player3_points = player_to_points[player3]
    # player4_points = player_to_points[player4]

    # if player1_points > player2_points and player1_points > player3_points and player1_points > player4_points:
    #     winner = player1
    # elif player2_points > player1_points and player2_points > player3_points and player2_points > player4_points:
    #     winner = player2
    # elif player3_points > player1_points and player3_points > player2_points and player3_points > player4_points:
    #     winner = player3
    # elif player4_points > player1_points and player4_points > player2_points and player4_points > player3_points:
    #     winner = player4
    # else:
    #     print("Its a tie/No one wins.... WOMP WOMP- Restart if you want")
    # return winner

#8
def get_best_word(players_words):
    best_Score = 0
    for word in players_words:
        points = get_points(word)
        if points > best_Score:
            best_Score = points
    return best_Score



num_players = int_input("Number of players: ")
player_to_words = {}
player_to_points = {}
player_to_hand = {}

for i in range(1, num_players + 1):
    name = str_input("Enter name of player {}: ".format(i))
    player_to_words[name] = []
    player_to_points[name] = 0
    player_to_hand[name] = get_new_tiles(7)

choice = None  # Initialize choice as None

# MAIN LOOP
while len(TILES) > 0 and choice != 1:
    print("---- NEW ROUND ----")
    for player in player_to_words:
        print("-- {}'s TURN --".format(player))
        print_hand(player_to_hand[player])
        print("Options for your turn:")
        print("0 - pick new tiles")
        print("1 - play word")
        print("Any other number - STOP GAME")
        choice = int_input("Enter a number to select: ")

        if choice == 0:
            TILES.extend(player_to_hand[player])
            player_to_hand[player] = get_new_tiles(7)
            print_hand(player_to_hand[player])
            print("END OF TURN")

        elif choice == 1:
            word = str_input("Enter the word to play: ")
            if not is_valid_play(word, player_to_hand[player]):
                print("INVALID GUESS - TURN SKIPPED")
            else:
                player_to_words[player].append(word)
                points = get_points(word)
                print("Your word earned", points, "points!")
                player_to_points[player] += points
                for char in word:
                    player_to_hand[player].remove(char)
                player_to_hand[player].extend(get_new_tiles(len(word)))
                print("UPDATED HAND:")
                print_hand(player_to_hand[player])

        else:
            print("STOPPING GAME...")
            break
print("GAME OVER - GENERATING GAME STATS")
print(get_winner(player_to_words ))
print(get_best_word(player_to_points))

