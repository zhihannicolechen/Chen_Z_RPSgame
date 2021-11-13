from random import randint
from gameComponents import winLose, gameVars
from gameComponents import comparison

print("++++++++++++ JOURNEY OF KITTY ++++++++++++")
print("Help Kitty defeat evil and protect the food!")
print("  _._     _,-'""`-._")
print(" (,-.`._,'(       | `-/|")
print("    `-.-'     )-`( , o o)")
print("-step-   `-      `_` = - ")
# set up our game loop so that we can keep playing and not exit
while gameVars.player is False:
    print("=======================================")
    gameVars.player = input("Choose your weapon: hammer, shield or sword: ")
    gameVars.computer = gameVars.choices[randint(0, 2)]

    print("player chose: " + gameVars.player)
    print("computer chose: " + gameVars.computer)

    comparison.comparison()

    print("fish of Kitty: " + str(gameVars.playerLives))
    print("Water cups of a human: " + str(gameVars.computerLives))

    if gameVars.playerLives == 0:
        winLose.winorlose("lost")

    elif gameVars.computerLives == 0:
        winLose.winorlose("won")

    gameVars.player = False
