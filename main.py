from random import randint
from gameComponents import winLose, gameVars

# set up our game loop so that we can keep playing and not exit
while gameVars.player is False:
    gameVars.player = input("Choose your weapon: rock, paper or scissors: ")
    gameVars.computer = gameVars.choices[randint(0, 2)]

    print("player chose: " + gameVars.player)
    print("computer chose: " + gameVars.computer)

    if gameVars.computer == gameVars.player:
        # tie - nothing else to compare, so it'll exit
        print("tie! try again")

    elif gameVars.player == "rock":
        if gameVars.computer == "paper":
            print("you lose!")
            gameVars.playerLives = gameVars.playerLives - 1
        else:
            print("you win!")
            gameVars.computerLives = gameVars.computerLives - 1

    elif gameVars.player == "paper":
        if gameVars.computer == "scissors":
            print("you lose!")
            gameVars.playerLives = gameVars.playerLives - 1
        else:
            print("you win!")
            gameVars.computerLives = gameVars.computerLives - 1

    elif gameVars.player == "scissors":
        if gameVars.computer == "rock":
            print("you lose!")
            gameVars.playerLives = gameVars.playerLives - 1
        else:
            print("you win!")
            gameVars.computerLives = gameVars.computerLives - 1

    print("player life count: " + str(gameVars.playerLives))
    print("computer life count: " + str(gameVars.computerLives))

    if gameVars.playerLives == 0:
        winLose.winorlose("lost")

    elif gameVars.computerLives == 0:
        winLose.winorlose("won")

    gameVars.player = False