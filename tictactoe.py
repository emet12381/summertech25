board = []
for i in range (3):
    slot = []
    for i in range (3):
        slot.append(" ")
    board.append(slot)
    

player = "X"
moves = 0
print (board [0][0]+" | "+ board [0][1]+ " | "+ board [0][2])
print("---------")
print (board [1][0]+ " | "+ board [1][1]+" | "+ board [1][2])
print ("---------")
print (board [2][0]+ " | "+ board [2][1]+" | "+ board [2][2])
while (moves >=0 and moves <9):
    row = int(input ("what row do you want to play in?"))
    col = int(input ("what column do you want to play in?"))
    board [row][col] = player
    moves = moves+1
    
    if board [0][0] == player and board [0][1] == player and board [0][2] == player:
        print("player", player, "wins!")
        moves = -1
    elif board [1][0] == player and board [1][1] == player and board [1][2] == player:
        print("player", player, "wins!")
        moves = -1
    elif board [2][0] == player and board [2][1] == player and board [2][2] == player:
        print("player", player, "wins!")
        moves = -1
    elif board [0][0] == player and board [1][0] == player and board [2][0] == player:
        print("player", player, "wins!")
        moves = -1
    elif board [0][1] == player and board [1][1] == player and board [2][1] == player:
        print("player", player, "wins!")
        moves = -1
    elif board [0][2] == player and board [1][2] == player and board [2][2] == player:
        print("player", player, "wins")
        moves = -1
    elif board [0][0] == player and board [1][1] == player and board [2][2] == player:
        print("player", player, "wins!")
        moves = -1
    elif board [0][2] == player and board [1][1] == player and board [2][0] == player:
        print("player", player, "wins!")
        moves = -1
    if moves == 9:
       print("it's a tie") 
       break
    print (board [0][0]+" | "+ board [0][1]+ " | "+ board [0][2])
    print("---------")
    print (board [1][0]+ " | "+ board [1][1]+" | "+ board [1][2])
    print ("---------")
    print (board [2][0]+ " | "+ board [2][1]+" | "+ board [2][2])
 

    if player == "X":
        player = "O"
    elif player == "O":
        player = "X"