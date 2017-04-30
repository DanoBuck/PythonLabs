def factorialRecursive(number):
    if number < 1:
        return 1
    return number * factorialRecursive(number-1)

# BE SURE TO CAST TO A LIST TO ENABLE PRINTING CONTENTS
listOfDigets = [1,2,3,4,5,6,7,8,9]
newList = list(map(factorialRecursive, listOfDigets))

print(newList)