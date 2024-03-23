"""
Problem 2: By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

def evenFibonacciSum(upperLimit: int = 4_000_000) -> int:
    """
    Find the sum of the even values in the fibonacci sequence up to the number entered.

    :param upperLimit: The limit to which the even-numbered sum should be found.
    :return: The sum of the even-numbered values in the fibonacci sequence up to the limit.
    """
    startingNumber = 0
    additiveNumber = 1
    sum = 0
    while(additiveNumber < upperLimit):
        placeholder = startingNumber
        startingNumber = additiveNumber
        additiveNumber += placeholder
        if(startingNumber % 2 == 0):
            sum += startingNumber

    return sum



limit = 1
while(limit != -1):
    try:
        limit = int(input("Enter a number; -1 to quit "))
    except:
        print("Not an integer.")
        quit()

    print(f"The sum of the even numbers in the fibonacci sequence up to {limit:,} is {evenFibonacciSum(limit):,}.\n")
    
quit()