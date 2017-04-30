def fibonacciSequence(numberElement):
    if numberElement == 0 or numberElement == 1:
        return numberElement
    else:
        return fibonacciSequence(numberElement - 1) + fibonacciSequence(numberElement - 2)

fibonacciList = []
for i in range(10):
    fibonacciList.append(fibonacciSequence(i))

print(fibonacciList)