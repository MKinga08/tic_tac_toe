
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
    elif 1 <= place <= 9 and board[place - 1] == choose:
        print("Position is taken")
        switch_player()
    return place


def is_valid(place):
    while True:
        if place < 1 or place > 9:
            print("Wrong input")
            switch_player()
            return False
        return True


def switch_player():
    global choose
    if choose.upper() == "X":
        choose = "O"
    else:
        choose = "X"
    return choose


def check_winner():
    if board[0] == choose and board[1] == choose and board[2] == choose \
            or board[3] == choose and board[4] == choose and board[5] == choose \
            or board[6] == choose and board[7] == choose and board[8] == choose \
            or board[0] == choose and board[3] == choose and board[6] == choose \
            or board[1] == choose and board[4] == choose and board[7] == choose \
            or board[2] == choose and board[5] == choose and board[8] == choose \
            or board[0] == choose and board[4] == choose and board[8] == choose \
            or board[2] == choose and board[4] == choose and board[6] == choose:
        print("You won")
        return True
    elif "_" not in board:
        print("Its a draw")
        return True
    return False


board = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
choose = choose_symbol()

def main():
    while True:
        create_board()
        position = players_choice()
        is_valid(position)
        if check_winner():
            create_board()
            break
        switch_player()


if __name__ == '__main__':
    main()
