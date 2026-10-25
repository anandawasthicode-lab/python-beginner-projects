bal=10000
att=0
corpin=1234
flag=0
tranh=[]
while att<3:
    att+=1
    userpin=int(input("enter the pin: "))
    
    if userpin==corpin and len(str(userpin))==4:
        while True:
            print('''1:show balance
2:deposit
3:withdraw
4:exit''')
            inpu=int(input("enter your choice :"))
            if inpu==1:
                print(bal)
            elif inpu==2:
                depo=int(input("enter the amt you want to deposit:"))
                bal+=depo
                print("your final balance is :",bal)
                tranh.append("deposited"+" "+str(depo)+" "+"balance"+" "+str(bal))
            elif inpu==3:
                wit=int(input("enter the amt you want to withdraw:"))
                if wit<=bal:
                    bal-=wit
                    tranh.append("withdrawal"+" "+str(wit)+" "+"balance"+" "+str(bal))
                    print("your final bal is ;",bal)
                else:
                    print("insufficient amt")
            elif inpu==4:
                flag=1
                break
            else:
                print("invalid input")
    if flag==1:
        print("Transaction History ")
        for i in tranh:
            print(i)  
        print("THANK YOU!")
        print("final balance: ",bal)
        break
    else:
        print("Try again")
else:
    print("Card blocked")


















