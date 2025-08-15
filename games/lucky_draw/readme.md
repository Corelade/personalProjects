# Lucky Draw (CLI)

A fast, lightweight command-line “last person standing” game. You pick a number; a random red ball number is drawn; if your pick matches the red ball, you’re eliminated. Survive the rounds until only one player remains.

# Features

1. Human vs. AI opponents (you choose the number of AIs)

2. Clean input validation with friendly prompts

3. Quit at any prompt by typing q

4. Simple, dependency-free Python

# How to Play

1. Choose opponents
    You’ll be asked how many AI opponents you want (between 5 and 9).

2. Enter a username
    Your name appears among the players.

3. Rounds

    - The game shuffles the players.

    - It generates a list of numbers from 1 to the number of remaining players.

    - One of those numbers becomes the red ball (secret).

    - Each player (AIs auto-pick; you choose) selects a number from the available options.

    - If a player’s pick equals the red ball, that player is eliminated.

    - Numbers picked are removed from the options (no duplicates that round).

    - Repeat until only one player remains — the winner.