from functools import reduce

def capitaliseWord(stringIn, index):
    if index % 2 == 0:
        return str.upper(stringIn)
    return stringIn

print(capitaliseWord("capitalise me", 0))

def swapCase(stringIn):
    splitStr = str.split(stringIn, " ")
    iterable = []
    iterable.extend(range(0, len(splitStr)))
    joinedString = " ".join(list(map(capitaliseWord, splitStr, iterable)))
    print (joinedString)

swapCase("hey gurl, lets javascript together sometime")

def shiftLetters(stringIn):
    letterList = list(stringIn)
    joined = "".join(list(map(lambda i: chr(ord(i) + 1), letterList)))
    return joined

print(shiftLetters("hello"))
print(shiftLetters("abcxyz"))

strings = ["Hello", "I", "Want", "You", "Reduced"]
reduced = reduce(lambda i, j: capitaliseWord(i, 0) + " " + capitaliseWord(j, 0), strings)
print(reduced)