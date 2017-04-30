def isPerfectNumber(number):
	result = 0
	for i in range(1, number):
		if number % i == 0:
			result += i
	return result == number
	
print(isPerfectNumber(6))
print(isPerfectNumber(5))
print(isPerfectNumber(28))
print(isPerfectNumber(496))
print(isPerfectNumber(8))
print(isPerfectNumber(8128))
print(isPerfectNumber(33550336))