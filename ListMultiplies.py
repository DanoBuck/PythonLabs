from functools import reduce

## REDUCE FUNCTION NEEDS 2 PARAMETERS TO DO ITS WORK
## REMEMBER THIS
def multiplyItemsReduce(a, b):
    if a == 0 and b == 0:
        return 0
    elif a != 0 and b == 0:
        return a
    elif a == 0 and b != 0:
        return b
    else:
        return a * b


print("*****Reduce*****")
list = [3,0,5]
result = reduce(multiplyItemsReduce, list)
print(result)

list = [2,4,5,0,0,0]
result = reduce(multiplyItemsReduce, list)
print(result)

## NON REDUCE FUNCTION
def multiplyItemsInList(list):
    multiply = 1
    for i in list:
        if(i != 0):
            multiply *= i

    return multiply

print("\n*****Non-Reduce*****")

list = [3,0,5]
print(multiplyItemsInList(list))

list = [2,4,5,0]
print(multiplyItemsInList(list))

# Filtering can remove 0's from the list and then apply a function
print("\n*****Filtering*****")
result = reduce(multiplyItemsReduce, filter(lambda i: i != 0, list))
print(result)

list = [3,0,5]
result = reduce(multiplyItemsReduce, filter(lambda i: i != 0, list))
print(result)

print("\n*****Multiplying Recursively*****")
def multiplyRecursively(list):
    if len(list) == 0:
        return 1
    if list[0] != 0:
        return list[0] * multiplyRecursively(list[1::])
    else:
        return multiplyRecursively(list[1::])

list = [2,4,5,0]
print(multiplyRecursively(list))
list = [3,0,5]
print(multiplyRecursively(list))