import tkinter #tk_interface




def new_game():
    global turns,game_over,label
    turns = 0
    game_over = False

    label.config(text=curr_player+"'s turn",foreground=color_white)

    for row in range(3):
        for column in range(3):
            board[row][column].config(text="",foreground=color_blue, background=color_grey)


#game set_up
playerX = "X"
playerO = "O"
curr_player = playerX
board = [[0,0,0],
         [0,0,0],
         [0,0,0]]
color_blue = "#4584b6"
color_yellow = "#ffde57"
color_grey = "#343434"
color_light_grey = "#646464"
color_red = "#ff0000"
color_white = "#ffffff"

turns = 0
game_over = False





def set_title(row,column):
    global curr_player

    if board[row][column]["text"] != "":
        return #already taken the spot


    board[row][column]["text"] = curr_player #mark the board

    if curr_player == playerO: #switchplayer
        curr_player = playerX
    else:
        curr_player = playerO

    label["text"] = curr_player+"'s turn"

    #check winner
    check_winner()

def check_winner():
    global turns,game_over
    turns +=1

    #horizontally , check 3 rows
    for row in range(3):
        if (board[row][0]["text"]== board[row][1]["text"] == board[row][2]["text"]
            and board[row][0]["text"] != ""):
            label.config(text=board[row][0]["text"] + " is the winner!", foreground=color_yellow)
            for column in range(3):
                board[row][column].config(foreground=color_yellow, background=color_light_grey)
            game_over = True
            return
   #vertically
    for column in range(3):
        if (board[0][column]["text"]== board[1][column]["text"] == board[2][column]["text"]
            and board[0][column]["text"] != ""):
            label.config(text=board[column][0]["text"] + " is the winner!", foreground=color_yellow)
            for row in range(3):
                board[row][column].config(foreground=color_yellow, background=color_light_grey)
            game_over = True
            return

#diagonally
    if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"]
        and board[0][0]["text"] != ""):
        label.config(text=board[0][0]["text"] + " is the winner!", foreground=color_yellow)
        for i in range(3):
             board[i][i].config(foreground=color_yellow, background=color_light_grey)
        game_over = True
        return
   #anti_diagonality
    if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"]
        and board[0][2]["text"] != ""):
        label.config(text=board[0][2]["text"] + " is the winner!", foreground=color_yellow)
        board[0][2].config(foreground=color_yellow, background=color_light_grey)
        board[1][1].config(foreground=color_yellow, background=color_light_grey)
        board[2][0].config(foreground=color_yellow, background=color_light_grey)
        game_over = True
        return



   #tie
    if turns == 9:
        game_over = True
        label.config(text="Tie", foreground=color_yellow)


#window
window = tkinter.Tk() #create game window
window.title("Tic Tac Toe")
window.resizable(False, False)


frame = tkinter.Frame(window)
label = tkinter.Label(frame,text=curr_player+"'s turn",font=("consolas",20),background=color_white,foreground=color_red)
label.grid(row=0,column=0 , columnspan=3 ,sticky="we")
button =  tkinter.Button(frame, text="restart", font=("consolas",20) , background=color_grey, foreground="white", command=new_game )
button.grid(row=4,column=0 , columnspan=3 ,sticky="we")
for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame, text="", font=("consolas",50,"bold"), background=color_grey,foreground=color_red,width=4,height=1,command=lambda row=row, column=column: set_title(row,column))

        board[row][column].grid(row=row+1,column=column)



frame.pack()

#center the window
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

#format(w)*(h)+(x)+(y)
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")



window.mainloop()
