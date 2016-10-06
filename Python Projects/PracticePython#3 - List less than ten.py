a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []

numberCeiling = int(input ("Please input a number: "))

for x in a:
    if x <= numberCeiling:
        b.append(x)

print (b)