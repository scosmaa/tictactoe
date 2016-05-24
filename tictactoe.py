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
        elif (o == 3)
            winner = "O"
    return (winner, remaining_moves)

def check_horizontal_rows(table):
    return check_rows(table)

def check_vertical_rows(table):
    inverted_table = [[table[0][index],table[1][index],table[2][index]] for index in range(0,3)]
    return check_rows(inverted_table)
    
def check_oblique_rows(table):
    oblique_rows = [[table[0][0],table[1][1],table[2][2]], [table[-1][-1],table[-2][-2],table[-3][-3]] 
    return check_rows(oblique_rows)
    
# Ask players name
players = {"X": raw_input("Enter PLAYER ONE name: "), "O": raw_input("Enter PLAYER TWO name: ")}
current_player = "X"

# Init a 3x3 matrix
table = [x[:] for x  in [[None] * 3] * 3]

print "Hi {0} and {1}! {2}".format(players["X"], players["O"],table[0][0])

#while !par():
    # ask current player next move
move = raw_input("{0}, it's your turn! [x-y]: ".format(players[current_player]))
x , y = move.split("-")

table[int(x)][int(y)] = current_player
table[0][1] = "O"
print check_horizontal_par(table) + check_vertical_par(table)
    # insert symbol into the table
    
    # set next player
        

    