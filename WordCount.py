from functools import reduce

def countWordsReduce(a, b):
    return a + 1

listOfWords = ["I", "went", "to", "the", "shops", "and", "this", "is", "great"]
result = reduce(countWordsReduce, filter(lambda i: i != "the" and i != "is" and i != "and", listOfWords), 0)

print("RESULT USING REDUCE AND FILTER:", result)

def countWordIterative(listOfWords):
    count = 0
    for i in listOfWords:
        if i != "the" and i != "and" and i != "is":
            count += 1

    return count

print("\nRESULT USING ITERATIVE APPROACH:", countWordIterative(listOfWords))

def countWordsRecursively(wordList):
    wordList = list(filter(lambda i: i != "the" and i != "and" and i != "is", wordList))
    if len(wordList) == 0:
        return 0
    return 1 + countWordsRecursively(wordList[1::])

print("\nRESULT USING RECURSIVE APPROACH WITH FILTERING:", countWordsRecursively(listOfWords))