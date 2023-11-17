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

connect_list = [{
    "Row1": ["0", "0", "0", "0", "0", "0", "0"],
    "Row2": ["0", "0", "0", "0", "0", "0", "0"],
    "Row3": ["0", "0", "0", "0", "0", "0", "0"],
    "Row4": ["0", "0", "0", "0", "0", "0", "0"],
    "Row5": ["0", "0", "0", "0", "0", "0", "0"],
    "Row6": ["0", "0", "0", "0", "0", "0", "0"]
}] # Represents a connect-4 board. 7L x 6H, List of lists.

# List goes from left to right. Row 1 is top, row 6 is bottom.
# Get element num by connect_list[0][Row_X][* PieceNum], * 0 being 1, 1 being 2, so on

def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

def printboard():
    final = ""
    for x in connect_list[0]: # Gets values of each row. Row1, Row2, etc
        data = connect_list[0]
        for num in range(7):
            final += f"{data[x][num]}"
        #final += f"{data[x][0]}{data[x][1]}{data[x][2]}{data[x][3]}{data[x][4]}{data[x][5]}{data[x][6]}"
        final += "\n"
    final = final.replace("0", emojis[0]["empty"]).replace( "1", emojis[0]["player1"]).replace("2", emojis[0]["player2"]) # Replaces numbers with emojis
    # Yellow is player 1        Red is player 2
    return final

def userinput(columnumber, player):
    columnumber = columnumber - 1
    if connect_list[0]["Row6"][columnumber] == "0":
        connect_list[0]["Row6"][columnumber] = player
    else: # Put in decending order, since that's how connect-4 is played
        if connect_list[0]["Row5"][columnumber] == "0":
            connect_list[0]["Row5"][columnumber] = player
        elif connect_list[0]["Row4"][columnumber] == "0":
            connect_list[0]["Row4"][columnumber] = player
        elif connect_list[0]["Row3"][columnumber] == "0":
            connect_list[0]["Row3"][columnumber] = player
        elif connect_list[0]["Row2"][columnumber] == "0":
            connect_list[0]["Row2"][columnumber] = player
        elif connect_list[0]["Row1"][columnumber] == "0":
            connect_list[0]["Row1"][columnumber] = player
        else:
            return False # Column is full!

def checkforwin():
    data = connect_list[0]
    for row in connect_list[0]:
        for col in range(7):
            #TODO

            if data[row][col] == "1": # PLAYER 1 WINS HORIZONTALLY
                if data[row][col+1] == "1":
                    if data[row][col+2] == "1":
                        if data[row][col+3] == "1":
                            print("Player 1 wins!!!")
                            exit()
                if data[row][col-1] == "1":
                    if data[row][col-2] == "1":
                        if data[row][col-3] == "1":
                            print("Player 1 wins!!!")
                            exit()

            if data[row][col] == "2": # PLAYER 2 WINS HORIZONTALLY
                if data[row][col+1] == "2":
                    if data[row][col+2] == "2":
                        if data[row][col+3] == "2":
                            print("Player 2 wins!!!")
                            exit()
                if data[row][col-1] == "2":
                    if data[row][col-2] == "2":
                        if data[row][col-3] == "2":
                            print("Player 2 wins!!!")
                            exit()

    return

def main():
    time.sleep(1)
    print("What's your name, player 1? (Yellow)")
    player1name = input(">> ")
    time.sleep(1)
    print("\nWhat's your name, player 2? (Red)")
    player2name = input(">> ")
    time.sleep(1)
    clear()

    i = 0
    while True:
        print("What column would you like to place your piece in?")
        if i % 2 == 0:
            player = "1" # Number is even, player 1 turn
            print(f'<<< Your move, {player1name} >>>\n')
        else:
            player = "2" # Number is odd, player 2 turn
            print(f'<<< Your move, {player2name} >>>\n')

        print("1️⃣ 2️⃣ 3️⃣ 4️⃣ 5️⃣ 6️⃣ 7️⃣\n") # Column numbers for the board
        print(printboard()) # Prints the current connect-4 board
        while True:
            try:
                cnum = int(input(">> ")) # Cnum is the column number
            except:
                print('Please enter a valid input!\n')
                continue
            if cnum >= 1 and cnum <=7:
                if userinput(cnum, player) == False:
                    print(f"Column #{cnum} is full! Please enter a different column.\n")
                    continue
                break
            else:
                print('Please enter a column number 1 through 7.\n')

        #print("----------------------------------------------")

        checkforwin()
        clear()
        i += 1

print('Welcome to Connect-4!\n')
main()
