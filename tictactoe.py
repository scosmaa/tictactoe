# Ask players name

def par():
    return True

players = {"X": raw_input("Enter PLAYER ONE name: "), "O": raw_input("Enter PLAYER TWO name: ")}
current_player = "X"

table =[[],[],[]],[[],[],[]],[[],[],[]]



print "Hi {0} and {1}! {2}".format(players["X"], players["O"],table[0][0])

#while !par():
    # ask current player next move
move = raw_input("{0}, it's your turn! [x-y]: ".format(players[current_player]))
x , y = move.split("-")

table[int(x)][int(y)] = current_player

print table[int(x)][int(y)]
    # insert symbol into the table
    
    # set next player
        
