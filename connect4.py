# 0 for empty
# 1 for player 1
# 2 for player 2
import os
import time

emojis = [
    {
        "empty": "🟦",
        "player1": "🟨",
        "player2": "🟥",
        "winning": "🟩"
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
    print("1️⃣ 2️⃣ 3️⃣ 4️⃣ 5️⃣ 6️⃣ 7️⃣\n") # Column numbers for the board
    final = ""
    for x in connect_list[0]: # Gets values of each row. Row1, Row2, etc
        data = connect_list[0]
        for num in range(7):
            final += f"{data[x][num]}"
        final += "\n"
    e = emojis[0]
    final = final.replace("0", e["empty"]).replace( "1", e["player1"]).replace("2", e["player2"]) # Replaces numbers with emojis
    return final

def userinput(columnumber, player): # Essentially the move function, places player on the board
  columnumber = columnumber - 1
  for row in range(6, 0, -1):
      if connect_list[0][f"Row{row}"][columnumber] == "0":
          connect_list[0][f"Row{row}"][columnumber] = player
          return True  # Successfully placed the piece
  return False # If we reach this point, it means the column is full

def checkforwin():
  data = connect_list[0]
  
  for row in range(1, 7):
      for col in range(7):
          player = data[f"Row{row}"][col]
          if player != "0":
              # Check horizontally
              if col + 3 < 7 and all(data[f"Row{row}"][col + i] == player for i in range(4)):
                  return True
              # Check vertically
              if row + 3 < 7 and all(data[f"Row{row + i}"][col] == player for i in range(4)):
                  return True
              # Check diagonally (up-right)
              if col + 3 < 7 and row + 3 < 7 and all(data[f"Row{row + i}"][col + i] == player for i in range(4)):
                  return True
              # Check diagonally (up-left)
              if col - 3 >= 0 and row + 3 < 7 and all(data[f"Row{row + i}"][col - i] == player for i in range(4)):
                  return True
  
  return False # Column is full!

def main():
    time.sleep(1)
    print("What's your name, player 1?")
    player1name = input(">> ")
    time.sleep(1)
    print("\nWhat's your name, player 2?")
    player2name = input(">> ")
    time.sleep(1)
    print(f"\nHello {player1name.title()} and {player2name.title()}!")
    time.sleep(1)
    print("Loading the board...")
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

        print(printboard()) # Prints the current connect-4 board
        while True: # Makes sure that the input is a valid integer, from 1 to 7
            try:
                cnum = int(input(">> ")) # Cnum is the column number
            except:
                print('Please enter a valid input!\n')
                continue
            if cnum >= 1 and cnum <=7:
                if userinput(cnum, player) == False: # Runs the user input, if it returns false, the column is full
                    print(f"Column #{cnum} is full! Please enter a different column.\n")
                    continue
                break
            else:
                print('Please enter a column number 1 through 7.\n')

        if checkforwin() == True:
            clear()
            print(printboard())
            print(f"<<< Player {player} wins!!! >>>")
            exit()
        clear()
        i += 1 # Add 1 for each turn

clear()
print('Welcome to Connect-4!\n')
main()
