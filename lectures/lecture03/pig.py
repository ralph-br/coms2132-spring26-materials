import random

def display_rules(): 
    print("""A player repeatedly rolls a die until a 1 is rolled or they choose to "hold":
    If the player rolls a 1, they score nothing in the run.
    If the player rolls any other number, it is added to their running total, and the player continues.
    If the player "holds", their total for this run is added to their score, and it becomes the other player's turn.
    The first player to score 100 or more points wins.
    """)

def announce_winner(player1_total, player2_total):
    if player1_total > player2_total: 
        print("Player 1 wins.") 
    else:
        print("Player 2 wins.")

def roll_die():
    # generated using GPT-4o, prompt: 
    # "write a python function roll_die() that rolls a single six-sided die and returns the number of eyes as an integer"
    return random.randint(1, 6)

def player_run():
    score = 0

    another = True
    while another: 
        eyes = roll_die()    
        print(f"Rolled: {eyes}")
        if eyes == 1:
            return 0 
        score += eyes
        print(f"Score for this run: {score}")
        choice = None # used for input verification
        while choice != "y" and choice != "n":
            choice = input("roll again (y/n)?")
        if choice == "n":
            another = False 
    
    return score 


def pig_game(): 
    
    display_rules()

    player1_total = 0 
    player2_total = 0
    while player1_total < 100 and player2_total < 100: 
        print(f"Player 1 total: {player1_total}")
        print(f"Player 2 total: {player2_total}")

        print("Player 1 turn")
        player1_total += player_run()
        if player1_total < 100: # interrupt if player1 reaches 100
            print("Player 2 turn")
            player2_total += player_run()

    print(f"Player 1 total: {player1_total}")
    print(f"Player 2 total: {player2_total}")    
    announce_winner(player1_total, player2_total)


if __name__ == "__main__":
    pig_game()