inputedNumber = int(input ("Please input a number:  "))
inputedCheck = int(input ("Please input a second number: "))
resultCheck = inputedNumber % inputedCheck

if resultCheck == 0:
    print (inputedNumber, "is divisible by", inputedCheck)

    if inputedNumber % 4 == 0:
        print (inputedNumber, "is also a multiple of 4")
else:
    print (inputedNumber, "is not divisible by", inputedCheck)

    if inputedNumber % 4 == 0:
        print (inputedNumber, "is also a multiple of 4")
