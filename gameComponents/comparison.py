import colorama
from gameComponents import gameVars

def comparison():
    if gameVars.computer == gameVars.player:
        # tie - nothing else to compare, so it'll exit
        print("tie! try again")

    elif gameVars.player == "hammer":
        if gameVars.computer == "Shield":
            print("you lose!")
            gameVars.playerLives = gameVars.playerLives - 1

        else:
            print("you win!")
            gameVars.computerLives = gameVars.computerLives - 1

    elif gameVars.player == "Shield":
        if gameVars.computer == "sword":
            print("you lose!")
            gameVars.playerLives = gameVars.playerLives - 1
        else:
            print("you win!")
            gameVars.computerLives = gameVars.computerLives - 1

    elif gameVars.player == "sword":
        if gameVars.computer == "hammer":
            print("you lose!")
            gameVars.playerLives = gameVars.playerLives - 1
    else:
        print("you win!")
        gameVars.computerLives = gameVars.computerLives - 1
