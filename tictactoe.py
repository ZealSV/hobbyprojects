print("Welcome to Tic Tac Toe!")
print("The rules are simple. The program will tell you which player starts first. Player X or Player O.")
print("When it's your turn, mark a location on the board where you want to place your X or O!")
print("You do this with the keybinds below, each representing a portion of the square in order.")
print("q w e")
print("a s d")
print("z x c")
print("Have fun!")

# were using the keyboard to assign a value to each number to mark the space.

theGame = {"q": "", "w": "", "e": "", "a": "", "s": "", "d": "", "z": "", "x": "", "c": ""}
board_command = []

#if (sum key entered)
#   put x in spot via. qwe asd zxc
#   print board
#   switch player

for key in theGame:
    board_command.append(key)

def displayGame(board):
    print(board["q"] + " / " + board["w"] + " / " + board["e"])
    print("------")
    print(board["a"] + " / " + board["s"] + " / " + board["d"])
    print("------")
    print(board["z"] + " / " + board["x"] + " / " + board["c"])

def checkGameWinner(counter, player):
    if counter >= 5:
        if theGame["z"] == theGame["x"] == theGame["c"] != "":
            displayGame(theGame)
            print("Game over! Player " + player + " won!")
            return True
        elif theGame["a"] == theGame["s"] == theGame["d"] != "":
            displayGame(theGame)
            print("Game over! Player " + player + " won!")
            return True
        elif theGame["q"] == theGame["w"] == theGame["e"] != "":
            displayGame(theGame)
            print("Game over! Player " + player + " won!")
            return True
        elif theGame["q"] == theGame["s"] == theGame["c"] != "":
            displayGame(theGame)
            print("Game over! Player " + player + " won!")
            return True
        elif theGame["z"] == theGame["s"] == theGame["e"] != "":
            displayGame(theGame)
            print("Game over! Player " + player + " won!")
            return True
        elif theGame["w"] == theGame["s"] == theGame["x"] != "":
            displayGame(theGame)
            print("Game over! Player " + player + " won!")
            return True
        elif theGame["q"] == theGame["a"] == theGame["z"] != "":
            displayGame(theGame)
            print("Game over! Player " + player + " won!")
            return True
        elif theGame["e"] == theGame["d"] == theGame["c"] != "":
            displayGame(theGame)
            print("Game over! Player " + player + " won!")
            return True
    if counter == 9:
        print("Game over! It's a tie!")
        return True

def ticTacToe(player, player2, counter):

    for i in range(9):
        displayGame(theGame)
        print("Player " + player + " it is your turn, please move")
        turn = input()
        print("Player " + player + " has chosen spot " + turn)
        if theGame[turn] == "":
            theGame[turn] = player
            counter += 1
        else:
            print("That spot is already filled, please move again")
        displayGame(theGame)
        if checkGameWinner(counter, player) == True:
            break
        if counter == 9:
            print("Game over! It's a tie!")
            break
        print("Player " + player2 + " it is your turn, please move")
        turn = input()
        print("Player " + player2 + " has chosen spot " + turn)
        if theGame[turn] == "":
            theGame[turn] = player2
            counter += 1
        else:
            print("That spot is already filled, please move again")
        if checkGameWinner(counter, player2) == True:
            break

def play():
    player = "X"
    player2 = "O"
    counter = 0
    ticTacToe(player, player2, counter)

play()

#  if played types a letter, then we fill the spot. PLEASE ENTER LETTER: (enters letter)
# new spot filled out. after I do this I can complete the checker and the function to switch the
# players every turn.
# figured out how to make the spots marked w X now i need to implement a switching turn thing
# and then fix the game winner code
# i have made it switch but now i need it to stop once someone wins. because i have it repeat 9
# times, the amount of times a marker can be placed, we need to check after each turn if there is a win.
# okay, now i made it declare the winner, we now need the game to end when we have a winner.
# there is an error when player wins horizontally, fixed.
# game ends now since i added breaks
