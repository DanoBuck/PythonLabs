def primeNumber(number):
    divisions = []
    number = number
    for i in range(2, number+1):
        if number % i == 0:
            divisions.append(i)

    if len(divisions) == 1:
        return True
    return False

myPrimes = []
unPrimes = []
for i in range(2, 100):
    if primeNumber(i):
        myPrimes.append(i)
    else:
        unPrimes.append(i)


print("PRIME NUMBERS", myPrimes)
print("NOT PRIME NUMBERS", unPrimes)

