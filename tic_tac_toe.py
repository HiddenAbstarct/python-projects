#Final Project for Python Essentials 1 course in CiscoNetAcads

"""
test_data1 = [
    [["O","O","O"],[4,5,6],[7,8,9]],
    [[1,2,3],["O","O","O"],[7,8,9]],
    [[1,2,3],[4,5,6],["O","O","O"]],
    [["O",2,3],["O",5,6],["O",8,9]],
    [[1,"O",3],[4,"O",6],[7,"O",9]],
    [[1,2,"O"],[4,5,"O"],[7,8,"O"]],
    [["O",2,3],[4,"O",6],[7,8,"O"]],
    [[1,2,"O"],[4,"O",6],["O",8,9]]
]

test_data2 = [
    [["X","X","X"],[4,5,6],[7,8,9]],
    [[1,2,3],["X","X","X"],[7,8,9]],
    [[1,2,3],[4,5,6],["X","X","X"]],
    [["X",2,3],["X",5,6],["X",8,9]],
    [[1,"X",3],[4,"X",6],[7,"X",9]],
    [[1,2,"X"],[4,5,"X"],[7,8,"X"]],
    [["X",2,3],[4,"X",6],[7,8,"X"]],
    [[1,2,"X"],[4,"X",6],["X",8,9]]
]
"""

from random import choice

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    count_row = 0
    count_col = 0

    def slot():
        nonlocal count_row 
        nonlocal count_col
        val = board[count_row][count_col]
        count_col += 1
        if count_col == 3:
               count_col = 0
               count_row += 1
        return val

    print(f"""
    +-------+-------+-------+
    |       |       |       |
    |   {slot()}   |   {slot()}   |   {slot()}   |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |   {slot()}   |   {slot()}   |   {slot()}   |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |   {slot()}   |   {slot()}   |   {slot()}   |
    |       |       |       |
    +-------+-------+-------+
    """)


def enter_move(board):
    #Player_O
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board using "O" according to the user's decision.
    for i in range(3):
        try:
            user_move = int(input("Enter your move: "))
            
            for j in board:
                for k in j:
                    if user_move == k:
                        board[board.index(j)][j.index(k)] = "O"
                        return None
                           
            if i < 2:
                print("Invalid move")

            

                
            
        except:
            print("Invalid move")
    print("Opps, elapsed your chances.")
    return None


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers (indices).
    free_sqs = []
    for i in board:
        for j in i:
            if type(j) is int:
                free_sqs.append((board.index(i), i.index(j)))
            else:
                continue
    return free_sqs


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == sign:
            return sign
        elif board[0][i] == board[1][i] == board[2][i] == sign:
            return sign
        elif board[0][0] == board[1][1] == board[2][2] == sign:
            return sign 
        elif board[0][2] == board[1][1] == board[2][0] == sign:
            return sign


def draw_move(board):
    #Player_X
    #The function draws the computer's move and updates the board.
    try:
        comp_move = choice(make_list_of_free_fields(board))
    except IndexError:
        return
    row = 0
    col = 0
    act = True
    for i in comp_move:
        if act:
            row = i
            act = False
        else:
            col = i
    board[row][col] = "X"


def main():
    board = [[1,2,3], [4,5,6], [7,8,9]]

    print("Let the game begin")
    display_board(board)
    Sign = "X"

    for i in range(9):                          #Game runs nine times
        if Sign == "X":                         #Computer: Player_X
            draw_move(board)
            display_board(board)
            Sign = "O"
        elif Sign == "O":                       #Player_O  
            enter_move(board)
            display_board(board)
            Sign = "X"

        if i > 3:
            if victory_for(board, "O") == "O":
                print("Congratulations, You Won!")
                return None
            elif victory_for(board, "X") == "X":
                print("You Lost!")
                return None
            
    print("It's a Tie")
    
main()