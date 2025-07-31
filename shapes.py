# for i in range (3):
#     for i in range (3):
#         print ("* ", end= "")
#     print()
# for i in range (3):
#     for j in range (i+1):
#         print("* ", end="")
#     print()
for i in range (3):
    for j in range(3-1-i):
        print (" ", end="")
    for k in range (i+1):
        print ("* ", end="")
    print ()
for i in range (3):
    for k in range (1+i):
        print (" ", end="")
    for j in range (3-i-1):
        print ("* ", end="")
    print()