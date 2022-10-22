
board = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]

def create_board():

    print("| " + board[0] + " | " + board[1] + " | " + board[2] + " | ")
    print("-------------")
    print("| " + board[3] + " | " + board[4] + " | " + board[5] + " | ")
    print("-------------")
    print("| " + board[6] + " | " + board[7] + " | " + board[8] + " | ")

    

def choose_symbol():
    symbol = str(input('Choose a symbol: X or O:'))
    if symbol.upper() == 'X':
        print('You choose: X\nyou may begin the game')
        return 'X'
    elif symbol.upper() == 'O':
        print('You choose: O')
        return 'O'


def players_choice():
    place = int(input("Enter a number between 1-9:"))
    if 1 <= place <= 9 and board[place - 1] == '_':
        board[place-1] = choose.upper()
    else:
        print("Position is taken")
        switch_player()


def switch_player():

    global choose
    if choose.upper() == "X":
        choose = "O"
    else:
        choose = "X"
    return choose


def check_winner():
    if board[0] == choose and board[1] == choose and board[2] == choose and board[0] != "-" \
            or board[3] == choose and board[4] == choose and board[5] == choose and board[3] != "-"\
            or board[6] == choose and board[7] == choose and board[8] == choose and board[6] != "-"\
            or board[0] == choose and board[3] == choose and board[6] == choose and board[0] != "-"\
            or board[1] == choose and board[4] == choose and board[7] == choose and board[1] != "-"\
            or board[2] == choose and board[5] == choose and board[8] == choose and board[2] != "-"\
            or board[0] == choose and board[4] == choose and board[8] == choose and board[0] != "-"\
            or board[2] == choose and board[4] == choose and board[6] == choose and board[2] != "-":
        print("You won")
        return True

choose = choose_symbol()

while True:
    create_board()
    players_choice()
    check_winner()
    switch_player()


