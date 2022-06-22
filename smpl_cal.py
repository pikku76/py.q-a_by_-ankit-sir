print("**********CALCULATOR**********")

print("---enter your choice---")

while True:
    choice=input("1.add\n2.substraction\n3.multiplication\n4.division\nselect your choice--->")
        #for add
    if choice=='1':
        a=int(input("Enter your 1st number::"))
        b=int(input("Enter your 2nd number::"))
        c=a+b
        print("your solution is::",c)

        #For Substract
    elif choice=='2':
        a=int(input("Enter your 1st number::"))
        b=int(input("Enter your 2nd number::"))
        D=a-b
        print("your solution is::",D)


    #for multiply
    elif choice=='3':
        a=int(input("Enter your 1st number::"))
        b=int(input("Enter your 2nd number::"))
        e=a*b
        print("your solution is::",e)

        #For Division
    elif choice=='4':
        a=int(input("Enter your 1st number::"))
        b=int(input("Enter your 2nd number::"))
        f=a/b
        print("your solution is::",f)

    else:
       print("invalid saytax")