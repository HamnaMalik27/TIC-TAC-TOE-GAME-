board = []
for i in range(9):
    board.append(" ")


def print_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()


def check_winner():
    wins = [[0,1,2],[3,4,5],[6,7,8],
            [0,3,6],[1,4,7],[2,5,8],
            [0,4,8],[2,4,6]]

    for combo in wins:
        a = combo[0]
        b = combo[1]
        c = combo[2]

        if board[a] == board[b] and board[b] == board[c] and board[a] != " ":
            return board[a]

    # board full check
    full = True
    for i in range(9):
        if board[i] == " ":
            full = False

    if full == True:
        return "Draw"

    return None

def minimax(ismax):

    result = check_winner()

    if result == "X":
        return 1
    if result == "O":
        return -1
    if result == "Draw":
        return 0

    if ismax == True:
        best = -1000
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(False)
                board[i] = " "
                if score > best:
                    best = score
        return best

    else:
        best = 1000
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(True)
                board[i] = " "
                if score < best:
                    best = score
        return best


def computer_move():
    bestscore = -1000
    move = -1

    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            score = minimax(False)
            board[i] = " "
            if score > bestscore:
                bestscore = score
                move = i

    board[move] = "X"


while True:

    print_board()

    position = int(input("ENTER YOUR POSITION (0 - 8): "))

    if board[position] != " ":
        print("Invalid move!")
        continue

    board[position] = "O"

    if check_winner() != None:
        break

    computer_move()

    if check_winner() != None:
        break


print_board()

result = check_winner()

if result == "X":
    print("Computer wins")
elif result == "O":
    print("You win")
else:
    print("Draw")





