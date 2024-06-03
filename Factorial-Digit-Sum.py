"""
Problem 20: Find the sum of the digits in the number 100!.
Answer: 648
"""

def factorial(num: int = 100) -> int:
    product = 1
    for i in range(1, num+1):
        product *= i
    
    return product

product = factorial(100)
sumOfDigits = 0
for char in str(product):
    sumOfDigits += int(char)

print(sumOfDigits)