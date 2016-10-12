oddeven =int(input("please enter a number: \n"))
check = oddeven%2
four = oddeven %4
if check ==0:
    if four ==0:
        print("This Number is even and divisible by 4!")
    else:
        print("this number is even but not divisble by four")
else:
    print("this number is odd")