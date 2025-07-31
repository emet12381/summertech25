board = []
for i in range (3):
    slot = []
    for i in range (3):
        slot.append(" ")
    board.append(slot)
    

player = "X"
moves = 0
while (moves >=0 and moves <9):
    print (board [0][0]+" | "+ board [0][1]+ " | "+ board [0][2])
    print("---------")
    print (board [1][0]+ " | "+ board [1][1]+" | "+ board [1][2])
    print ("---------")
    print (board [2][0]+ " | "+ board [2][1]+" | "+ board [2][2])
    row = int(input ("what row do you want to play in?"))
    col = int(input ("what column do you want to play in?"))
    board [row][col] = player
    moves = moves+1
