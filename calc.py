while(True):
    num1=int(input("enter the first integer"))
    num2=int(input("enter the second integer"))
    operation=input("enter the operation")


    if operation == "+":
        print (num1+num2)

    elif operation == "-":
        print (num1-num2)
    elif operation == "*":
        print (num1*num2)
    elif operation == "/":
        if num2==0:
            print ("invalid divisor")
        else:
            print (num1/num2)
    else :
        print ("invalid operation")


    answer=input("do you want to do another calculation?")
    if answer == "no":
        break
