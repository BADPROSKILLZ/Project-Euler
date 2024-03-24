"""
Problem 16: What is the sum of the digits of the number 2^1000?
Answer: 1366
"""

def sumDigits(number: int) -> int:
    """
    Finds the sum of the digits of the number input.
    
    :param number: The number which to find the sum of the digits of.
    :return: The sum of the digits of the number input.
    """
    sum = 0
    for digit in str(number):
        sum += int(digit)
        
    return sum

print(sumDigits(2 ** 1000))