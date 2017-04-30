from random import uniform
from functools import reduce

def fahrenheitToCelsius(convert):
    return round((((convert - 32) * 5) / 9), 2)

print("*****FAHRENHEIT TO CELSIUS*****")
print(fahrenheitToCelsius(32))
print(fahrenheitToCelsius(68))

def celsiusToFahrenheit(convert):
    return round(((((convert * 9) / 5) + 32)), 2)

print("*****CELSIUS TO FAHRENHEIT*****")
print(celsiusToFahrenheit(0))
print(celsiusToFahrenheit(20))

def higherOrderFunction(function, parameterToApply):
    return function(parameterToApply)

print("*****HIGHER ORDER FUNCTION*****")
print(higherOrderFunction(fahrenheitToCelsius, 68))
print(higherOrderFunction(celsiusToFahrenheit, 20))

celsiusList = []
for i in range(5):
    celsiusList.append(round(uniform(1.0, 25.0), 2))

print("*****RANDOM CELSIUS LIST*****")
print(celsiusList)

averageTemperature = reduce(lambda a,b: a + b, celsiusList) / len(celsiusList)
print("Average temperature:",round(averageTemperature, 2))

def minTemp(a, b):
    if a < b:
        return a
    return b

minimumTemperature = reduce(min, celsiusList)
print("Minimum temperature:", minimumTemperature)

def maxTemp(a, b):
    if a > b:
        return a
    return b

maximumTemperature = reduce(max, celsiusList)
print("Maximum temperature:", maximumTemperature)

print("*****CELSIUS LIST TO FAHRENHEIT LIST*****")
print("As Celsius", celsiusList)
celsiusList = list(map(lambda i: higherOrderFunction(celsiusToFahrenheit, i), celsiusList))
print("As Fahrenheit", celsiusList)
