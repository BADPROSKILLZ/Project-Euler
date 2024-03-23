"""
Problem 1: Find the sum of all the multiples of 3 or 5 below 1000.
"""

def multiplesOf3And5(upperLimit: int = 1_000) -> int:
    """
    Finds the sum of all the multiples of 3 or 5 below the number entered.

    :param upperLimit: The limit to which the sum should be found.
    :return: The sum of all the multiples of 3 or 5 up to the limit.
    """
    sum = 0
    for num in range(upperLimit):
        if(num % 3 == 0 or num % 5 == 0):
            sum += num
    
    return sum


limit = 1
while(limit != -1):
    try:
        limit = int(input("Enter the upper limit; -1 to quit. "))
    except:
        print("Not an integer. ")
        quit()
    
    print(f"The sum of all the multiples of three and five up to {limit:,} is {multiplesOf3And5(limit):,}.\n")

quit()