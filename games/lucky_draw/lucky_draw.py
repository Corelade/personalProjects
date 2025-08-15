import random
import time


def get_numeric_input(prompt, low=5, high=9):
    while True:
        resp = input(prompt)

        if resp == 'q':
            exit()

        try:
            number = int(resp)
        except ValueError:
            print("Only numbers are allowed")
            continue

        if number < low or number > high:
            print(f"Number must be between {low} and {high}")
            continue
        return number


def game(players):
    
    def wrong_answer(red_ball, choice):
        return red_ball == choice

    # Loop until a winner is found
    winner = None
    while not winner:

        if len(players) == 1:
            winner = players[0]

        random.shuffle(players)

        # everyone should pick numbers that will represent index of items in list
        # the maximum number should be the len(players)
        options = [(i + 1) for i in range(len(players))]
        random.shuffle(options)

        # anyone that picks the same index as that of red_ball loses
        red_ball = random.choice(options)

        # since i'll be working with indexes, i have to subtract one from what anyone chooses
        for player in players:
            # print(f"Options to choose from are 1 and {len(options)}")
            # subtract the choice by 1 to get the index
            if "AI" not in player:
                if len(options) == 1:
                    user_choice = options[0]
                else:
                    user_choice = (
                        get_numeric_input(f"Choose a number in range {1} - {len(options)}, or q to quit:  ", 1, len(options)) - 1
                    )
                    user_choice = options[user_choice]
                if wrong_answer(red_ball, user_choice):
                    players.remove(player)
                    break
                options.remove(user_choice)
            else:
                ai_choice = random.choice(options)
                if wrong_answer(red_ball, ai_choice):
                    print(f'{player} Eliminated')
                    players.remove(player)
                    break
                options.remove(ai_choice)

    return winner


def play():
    "choose how many opponents you want in this game"
    opponent_count = get_numeric_input(
        "How many opponents do you want to play against (Select a number between 5 - 9)? or q to quit: ",
        5,
        9,
    )

    while True:
        username = input("Enter your username: ").strip()
        if not username:
            continue
        break
    
    def create_players(opponent_count):
        "create AI instances"
        ais = ["AI" + str(i) for i in range(1, opponent_count + 1)]

        players = ais + [username]
        
        return players

    while True:
        PLAYERS = create_players(opponent_count)
        winner = game(PLAYERS)
        print(f"winner is {winner}")


if __name__ == "__main__":
    print(play())
