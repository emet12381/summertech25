# cart = ["apple", "bannana", "pineapple", "chips", "parsley"]
# print (cart[len(cart)-1]) 
cart = []
# cart.append("pineapple")
# cart.append("parsley")
# print (cart)
while(True):
    item = input ("what would you like to add?")
    cart.append (item)
    print (cart)
    answer = input ("would you like to add another item?")
    if answer == ("no"):
        break