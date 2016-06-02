# check if the row contains a victory or its blocked
def check_rows(table):
    remaining_moves = 0
    winner = ""
    for row in table:
        x = o = 0
        # count occupied cells
        for col in row:
            if(col == "X"):
                x +=1
            elif(col == "O"):
                o += 1
        # check if the row is empty or has only one type signs 
        if(x == o == 0 or (x == 0 or o == 0 and x+0 <= 3)):
            remaining_moves += 1
        if (x == 3):
            winner = "X"
        elif (o == 3):
            winner = "O"
    return (winner, remaining_moves)
#fffff

def check_horizontal_rows(table):
    return check_rows(table)

def check_vertical_rows(table):
    inverted_table = [[table[0][index],table[1][index],table[2][index]] for index in range(0,3)]
    return check_rows(inverted_table)
    
def check_oblique_rows(table):
    oblique_rows = [[table[0][0],table[1][1],table[2][2]], [table[-1][-1],table[-2][-2],table[-3][-3]]] 
    return check_rows(oblique_rows)

def match_status(table):
    horizontal_status = check_horizontal_rows(table)
    vertical_status = check_vertical_rows(table)
    oblique_status = check_oblique_rows(table)
    
    winner = horizontal_status[0] + vertical_status[0] + oblique_status[0]
    ramaining_moves = horizontal_status[1] + vertical_status[1] + oblique_status[1]
    return (winner, ramaining_moves)

def print_table(table):
    for row in table:
        print row
    
    
# Ask players name
players = {"X": raw_input("Enter PLAYER ONE name: "), "O": raw_input("Enter PLAYER TWO name: ")}
current_player = "X"

# Init a 3x3 matrix
table = [x[:] for x  in [[None] * 3] * 3]

print "Hi {0} and {1}!".format(players["X"], players["O"])

status = ("", 8)

while (status[0] == "" and status[1] > 0 ):
    # ask current player next move
    move = raw_input("{0}, it's your turn! [x-y]: ".format(players[current_player]))
    x , y = move.split("-")
    table[int(x)][int(y)] = current_player
    print_table(table)
    current_player = "X" if current_player == "O" else "O"
    status = match_status(table)

if(status[0] != ""):
    print "Congratulations {0}. YOU WIN!".format(players[status[0]])
else:
    print "No more valid moves. End of the game!"
