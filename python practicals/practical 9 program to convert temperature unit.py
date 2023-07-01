while(1):
    print("1.celcius to farhenite\n 2.fahrenite to celcius\n 3.exit\n")
    choice=input("Enter your chice:")
    ch=int(choice)
    if(ch==1):
        c=int(input)("Enter the temperature in celcius:")
        f=((,*c)15)+32
        print("converted temperature is:",f)
    elif(ch==2):
        f=int(input("Enter the temperature in farhenite:"))
        c=((f-32)/9)*5
        print("converted temperature is:",c)
    elif(ch==3):
        exit()
    else
    print("wrong choice")
