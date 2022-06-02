import random

def play(): 
    possible_action = ['R', 'P', 'S']
    computer = random.choice(possible_action)
    player = input("Pick a weapon: 'R' for Rock, 'P' for paper, 'S' for scissors ").capitalize()

    while player not in possible_action:
        player = input('''Try again: Pick a weapon 'R' for rock, 'P' for paper, 'S' for scissors ''').capitalize()

    if player == computer:    
       print(f'player ({player}) : CPU ({computer})')
       print('Its a tie')
       return play()
    #r > s, s > p, p > r
    elif player == "R": 
        if computer == "P":
           print(f'player ({player}) : CPU ({computer})')
           print("LOSER!") 
        if computer == "S":
            print("WINNER!")
    elif player == "S":
        if computer == "R":
            print(f'player ({player}) : CPU ({computer})')
            print("LOSER!")
        if computer == "P":
            print(f'player ({player}) : CPU ({computer})')
            print("WINNER!")        

    elif player == "P":
        if computer == "S":
            print(f'player ({player}) : CPU ({computer})')
            print("LOSER!") 
        if computer == "R":
            print(f'player ({player}) : CPU ({computer})')
            print("WINNER!")
play()