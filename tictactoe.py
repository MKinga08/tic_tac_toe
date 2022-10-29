def create_board():
    print("| " + board[0] + " | " + board[1] + " | " + board[2] + " | ")
    print("-------------")
    print("| " + board[3] + " | " + board[4] + " | " + board[5] + " | ")
    print("-------------")
    print("| " + board[6] + " | " + board[7] + " | " + board[8] + " | ")


def symbol_validator():
    while True:
        symbol = input('Choose a symbol: X or O:').upper()
        if symbol.isalpha():
            if symbol == "X":
                return symbol
            elif symbol == "O":
                return symbol
            else:
                print("You have to choose between the given symbols")
        else:
            print("You have to choose the letter O or the letter X")


def choose_symbol(symbol):
    if symbol == 'X':
        print('You choose: X')
        return 'X'
    elif symbol == 'O':
        print('You choose: O')
        return 'O'


def input_validator():
    while True:
        place = input("Enter a number between 1-9:")
        if place == 'q':
            quit()
        if place.isnumeric():
            place = int(place)
            if place < 1 or place > 9:
                print("Input out of range")
            elif 1 <= place <= 9 and board[place - 1] == choose:
                print("Position is taken")
            else:
                return place
        else:
            print("Please enter a number")


def get_move(place):
    if 1 <= place <= 9 and board[place - 1] == '_':
        board[place - 1] = choose.upper()


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
player = symbol_validator()
choose = choose_symbol(player)


def main():
    while True:
        create_board()
        position = input_validator()
        get_move(position)
        if check_winner():
            create_board()
            break
        switch_player()


if __name__ == '__main__':
    main()
