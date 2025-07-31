# cart = ["apple", "bannana", "pineapple", "chips", "parsley"]
# print (cart[len(cart)-1]) 
cart = []
# cart.append("pineapple")
# cart.append("parsley")
# print (cart)




while(True):
    answer = input ("press a if you would like to add an item and press r if you would like to remove item")
    if answer == ("a"):
        item = input ("what would you like to add?")
        cart.append (item)
        print (cart)
    elif answer == ("r"):
        if len (cart) == 0:
            print ("the cart is empty")
            continue
        item = input("what would you like to remove?")
        cart.remove (item)
        print (cart)
    else:
        print ("invalid option")
        continue
    answer = input ("would you like to add or remove another item?")
    if answer == ("no"):
        break
     