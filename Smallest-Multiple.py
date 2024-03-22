"""
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

#make a function to check if some number is prime
def primeCheck(primeCandidate: int) -> bool:
    """
    Checks if the number input is prime.

    :param primeCandidate: Number to check prime status of.
    :return: Returns true if prime, false if composite.
    """
    isPrime = True
    for num in range(int(primeCandidate / 2)): #Check only first half, rest will be covered automatically
        num += 2
        if (primeCandidate % num == 0): #Check if num is a factor
            return False
        
    return isPrime


#make a function to get the prime numbers lower than the upper boundary
def getPrimes(upperBoundary: int = 20) -> list[int]:
    """
    Returns a list of prime numbers lower than the number input
    
    :param upperBoundary: Number to get primes up to.
    :return: Returns a list of prime numbers lower than the number input
    """
    
    lowerPrimes = []
    for num in range(2, upperBoundary+1):
        if(primeCheck(num) or num == 2):
            lowerPrimes.append(num)
    
    return lowerPrimes

#make a function to raise the prime numbers to the highest power that would result in an answer lower than the upper boundary 
def getPoweredPrime(base: int = 1, upperBoundary: int = 20) -> int:
    """
    Returns the base raised to the some power, which altogether is lower or equal to the upper boundary.
    
    :param base: Number to raise to a power.
    :param upperBoundary: Number which not to exceed.
    :return: Returns the base raised to the some power, which altogether is lower or equal to the upper boundary.
    """
    print("START")
    exponent = 0
    
    while(int(base ** exponent) <= upperBoundary):
        print(base ** exponent)
        exponent += 1
        
    
    exponent -= 1
    print("END")
    return int(base ** exponent)


#multiply all above numbers together
limit = 0
print("Hello World")
while(limit != -1):
    try:
        limit = int(input("Enter a number; -1 to quit "))
    except:
        print("Not an integer. ")
        quit()
    
    print(f'{limit}')
    primeList: list[int] = getPrimes(limit)
    leastCommonMultiple: int = 1
    print(len(primeList), primeList)
    for num in range(len(primeList)):
        primeList[num] = getPoweredPrime(primeList[num], limit)
        leastCommonMultiple *= primeList[num]
        
    print(f'The least common multiple of all numbers from 1-{limit} is {leastCommonMultiple}')
    
