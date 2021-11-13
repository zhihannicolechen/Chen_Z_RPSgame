from gameComponents import gameVars


def winorlose(status):
    print("you " + status)

    choice = input("Come and challege again! :) y/n: ")

    if choice == "n":
        print("======= Kitty say: Thank you for lending a helping hand ======")
        print("    | __/,|   (` MEOW! ")
        print("  _.|o o  |_   ) )")
        print("-(((---(((--------")
        exit()
    elif choice == "y":
        gameVars.playerLives = 2
        gameVars.computerLives = 2
        gameVars.player = False