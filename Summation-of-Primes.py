"""
Problem 10: Find the sum of all the primes below two million. Answer is 142913828922, ran overnight
"""

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

def findLesserPrimes(upperBoundary: int = 2_000_000) -> list[int]:
    """
    Gets a list of all prime numbers less than the parameter.
    
    :param upperBoundary: Number up to which to find primes.
    :return: Returns a list of all prime numbers less than the parameter.
    """
    primeArray = [2]
    for num in range(3, upperBoundary):
        if(primeCheck(num)):
            primeArray.append(num)
            print(num, end=" ")
    print("")
    
    return primeArray

userInput = 0
while(userInput != -1):
    try:
        userInput = int(input("Enter upper bound; -1 to exit "))
    except:
        print("Not an integer. ")
        quit()
    
    primes = findLesserPrimes(userInput)
    sum = 0
    for prime in primes:
        sum += prime
    
    print(sum)