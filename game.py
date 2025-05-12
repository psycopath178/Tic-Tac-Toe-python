import random
from tkinter import Tk, Frame, Label, Button

# Global variables
current_player = 'X'
player = ["X", "O"]
board_buttons = [[None for _ in range(3)] for _ in range(3)]  # For GUI buttons
logic_board = [[' ' for _ in range(3)] for _ in range(3)]    # For game logic

def check_winner(board, player):
    # Check rows
    for i in range(3):
        if all([cell == player for cell in board[i]]):
            return True
    
    # Check columns
    for i in range(3):
        if all([board[j][i] == player for j in range(3)]):
            return True
    
    # Check diagonals
    if all([board[i][i] == player for i in range(3)]):
        return True
    if all([board[i][2-i] == player for i in range(3)]):
        return True
    
    return False

def is_full(board):
    return all(cell != ' ' for row in board for cell in row)

def computer_move():
    global current_player, logic_board
    corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
    for i in range(3):
        for j in range(3):
            if logic_board[i][j] == ' ':
                logic_board[i][j] = 'O'
                if check_winner(logic_board, 'O'):
                    board_buttons[i][j].config(text='O')
                    return
                logic_board[i][j] = ' '
    for i in range(3):
        for j in range(3):
            if logic_board[i][j] == ' ':
                logic_board[i][j] = 'X'
                if check_winner(logic_board, 'X'):
                    logic_board[i][j] = 'O'
                    board_buttons[i][j].config(text='O')
                    return
                logic_board[i][j] = ' '
    if logic_board[1][1] == ' ':
        logic_board[1][1] = 'O'
        board_buttons[1][1].config(text='O')
        return
    for i, j in corners:
        if logic_board[i][j] == ' ':
            logic_board[i][j] = 'O'
            board_buttons[i][j].config(text='O')
            return
    for i in range(3):
        for j in range(3):
            if logic_board[i][j] == ' ':
                logic_board[i][j] = 'O'
                board_buttons[i][j].config(text='O')
                return

def newgame():
    global current_player, logic_board
    current_player = 'X'
    label.config(text=current_player + " turn")
    logic_board = [[' ' for _ in range(3)] for _ in range(3)]
    for row in range(3):
        for column in range(3):
            board_buttons[row][column].config(text="", bg="#F0F0F0")

def next_turn(row, column):
    global current_player
    
    if logic_board[row][column] == ' ' and not check_winner(logic_board, 'X') and not check_winner(logic_board, 'O'):
        logic_board[row][column] = current_player
        board_buttons[row][column].config(text=current_player)
        
        if check_winner(logic_board, current_player):
            label.config(text=f"{current_player} wins!")
            return
        
        if is_full(logic_board):
            label.config(text="Tie!")
            return
        current_player = 'O'
        label.config(text="Computer's turn")
        window.after(500, computer_turn)

def computer_turn():
    global current_player
    
    computer_move()
    if check_winner(logic_board, 'O'):
        label.config(text="Computer wins!")
        return
    
    if is_full(logic_board):
        label.config(text="Tie!")
        return
    
    current_player = 'X'
    label.config(text=f"{current_player}'s turn")
window = Tk()
window.title("TIC-TAC-TOE")

label = Label(text=current_player + " turn", font=('consolas', 40))
label.pack(side="top")

reset_button = Button(text="restart", font=('consolas', 20), command=newgame)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        board_buttons[row][column] = Button(
            frame, 
            text="", 
            font=('consolas', 40), 
            width=5, 
            height=2,
            command=lambda r=row, c=column: next_turn(r, c))
        board_buttons[row][column].grid(row=row, column=column)

window.mainloop()