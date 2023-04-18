for number in range (10,100):
    x = (number % 10)
    y = (number/7)
    
    if x == y:
        print((number),"Correct Number")
        magicnumber = (number)
    elif x != y:
        print((number),"Incorrect Number")

if number == 99:
    print()
    print("The correct number is,",(magicnumber))