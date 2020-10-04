 #display board first
# from IPython.display import clear_output

def display_board(boardList):
    # clear_output()
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

#define boardlist and the call the function 
board=["#","X","O","X","O","X","O","X","O","X"]
display_board(board)

# ask user for correct input
def user_input():
    marker=""
    while marker!="X" and marker!="O":
        marker= input("Player1: choose X or O: ").upper()
        if marker=="X":
            return("X","O")
        else:
            return("O","X")

#tuple unpacking
player1_marker,player2_marker=user_input()

