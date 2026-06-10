if(2!=3):
    print("Hello World")
    print(123)
else:
    print("This is else else condition")

if True:
    print("Only if condition")

print("This is outside the is condition")


if(1==1):
    print("if condition")

elif(2==2):
    print("elif condition")

else:
    print("else condition")

marks = 90
if(marks>=80):
    print("You have got A in your exam")
    if(marks==90):
        print("Lucky")
    elif(marks==100):
        print("Topper")

elif(marks>=60 and marks<=80):
    print("Well Done")
    if(1==1):
        print("This is true")

elif(marks>=50 and marks<=60):
    print("2nd Division")

else:
    print("Fail")


amount = 100
is_coupon = True
is_member = True
if(amount>=100):
    print("You have got a discount")
    if(is_member):
        print("member")
        if(is_coupon):
            print("You have got a 20% discount")
        else:
            print("5% discount")
    else:
        print("You have got the 10% discount")
else:
    print("You must buy 100 rupee to get discount")