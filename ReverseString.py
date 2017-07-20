def reverseString(reverseMe):
    string = ""
    for i in reversed(reverseMe):
        string += i
    return string


print("*****Reverse String Iteratively*****")
print(reverseString("Reverse Me"))

def reverseRecursively(reverseMe):
    if len(reverseMe) == 0:
        return ""
    return reverseMe[len(reverseMe)-1] + reverseRecursively(reverseMe[:len(reverseMe) - 1])

print("*****Reverse String Recursively*****")
print(reverseRecursively("Reverse Me"))
print(reverseRecursively("I want to be reversed recursively"))

def simpleReverse(string):
    return string[::-1]

print("*****Reverse String Array Negative Indexing*****")
print(simpleReverse("Reverse Me"))
print(simpleReverse("I want to be reversed recursively"))