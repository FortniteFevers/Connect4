# 0 for empty
# 1 for player 1
# 2 for player 2
import os
import time

emojis = [
    {
        "empty": "⬛️",
        "player1": "🟨",
        "player2": "🟥"
    }
]

connect_list = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
] # Represents a connect-4 board. 7L x 6H, List of lists.

# List goes from left to right. Row 1 is top, row 6 is bottom.
# Get element num by connect_list[0][Row_X][* PieceNum], * 0 being 1, 1 being 2, so on

def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

def printboard():
    final = ""
    for x in range(5): # Gets values of each row. Row1, Row2, etc
        data = connect_list
        for num in range(7):
            final += f"{data[x][num]}"
            if data[x][num] == 0:
                data[x][num] = emojis[0]["empty"]
            if data[x][num] == 1:
                data[x][num] = emojis[0]["player1"]
            if data[x][num] == 2:
                data[x][num] = emojis[0]["player2"]
        #final += f"{data[x][0]}{data[x][1]}{data[x][2]}{data[x][3]}{data[x][4]}{data[x][5]}{data[x][6]}"
        final += "\n"

    
    #final = final.replace(0, emojis[0]["empty"]).replace(1, emojis[0]["player1"]).replace(2, emojis[0]["player2"]) # Replaces numbers with emojis
    # Yellow is player 1        Red is player 2
    return final

def userinput(columnumber, player):
    columnumber = columnumber - 1
    if connect_list[5][columnumber] == 0:
        connect_list[5][columnumber] = player
    else: # Put in decending order, since that's how connect-4 is played
        if connect_list[4][columnumber] == 0:
            connect_list[4][columnumber] = player
        elif connect_list[3][columnumber] == 0:
            connect_list[3][columnumber] = player
        elif connect_list[2][columnumber] == 0:
            connect_list[2][columnumber] = player
        elif connect_list[1][columnumber] == 0:
            connect_list[1][columnumber] = player
        elif connect_list[0][columnumber] == 0:
            connect_list[0][columnumber] = player

def checkforwin():
    data = connect_list
    for row in range(6):
        for col in range(7):
            #TODO

            if data[row][col] == 1: # PLAYER 1 WINS
                if data[row][col+1] == 1:
                    if data[row][col+2] == 1:
                        if data[row][col+3] == 1:
                            print("Player 1 wins!!!")
                            exit()
                if data[row][col-1] == 1:
                    if data[row][col-2] == 1:
                        if data[row][col-3] == 1:
                            print("Player 1 wins!!!")
                            exit()
                            
            if data[row][col] == 2: # PLAYER 2 WINS
                if data[row][col+1] == 2:
                    if data[row][col+2] == 2:
                        if data[row][col+3] == 2:
                            print("Player 2 wins!!!")
                            exit()
            
    return

def main():
    i = 0
    while True:
        if i % 2 == 0:
            player = 1 # Number is even, player 1 turn
        else:
            player = 2 # Number is odd, player 2 turn

        print("What column would you like to place your piece in?")
        print(f'<<< Your move, player {player} >>>\n')
        print("1️⃣ 2️⃣ 3️⃣ 4️⃣ 5️⃣ 6️⃣ 7️⃣\n") # Column numbers for the board
        print(printboard()) # Prints the current connect-4 board
        while True:
            try:
                cnum = int(input(">> ")) # Cnum is the column number
            except:
                print('Please enter a valid input!')
            if cnum >= 1 and cnum <=7:
                break
            else:
                print('Please enter a column number 1 through 7.')

        #print("----------------------------------------------")

        userinput(cnum, player)
        checkforwin()
        clear()
        i += 1

print('Welcome to Connect-4!\n')
main()
