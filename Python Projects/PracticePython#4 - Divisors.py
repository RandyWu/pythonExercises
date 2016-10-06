num = int(input ("Please input a number: "))

numList = range(1, num + 1)
solutionList = []

for x in numList:
    if num % x == 0:
        solutionList.append(x)

print (solutionList)
