# Summing of numbers in a list Iteratively
listOfNumbers = [5,20,25,30]
listSum = 0
for x in listOfNumbers:
	listSum += x

print("********Iterative Sum********")
print(listSum)

# Summing of numbers in a list using top level functions
print("********Built in Sum********")
print(sum(listOfNumbers))

def recursiveSum(list):
	if len(list) == 0:
		return 0
	return list[0] + recursiveSum(list[1::])

print("********Recursive Sum********")
print(recursiveSum(listOfNumbers))