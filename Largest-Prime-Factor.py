"""
Find the largest prime factor of 600851475143
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


primeCandidate = 1
while(primeCandidate != -1):
    try:
        primeCandidate = int(input("Enter a number; -1 to quit "))
    except:
        print("Not an integer.")
        quit()
    
    upperBound = primeCandidate
    for possibleFactor in range(upperBound): #For all numbers up to the current upper bound
        if (possibleFactor <= upperBound): #As long as the possible factor is less than the current bound
            possibleFactor += 1 
            if ((primeCandidate / possibleFactor) % 1 != 0):
                continue

            upperBound = primeCandidate / possibleFactor
            print(possibleFactor, primeCheck(possibleFactor), upperBound, primeCheck(upperBound))
    print("\n")

quit()
