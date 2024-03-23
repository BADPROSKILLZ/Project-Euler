"""
Find the 10_001st prime number.
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

#outer loop from 1-10_001 to count num of primes found
    #inner loop to check if 

primeArray = [0]*10001 
primeArray[0], primeArray[1], primeArray[2] = 2, 3, 5
testNum = 5
for prime in range(3, len(primeArray)):
    while(primeArray[prime] == 0):
        testNum += 2
        if(testNum % 5 != 0 and primeCheck(testNum)):
            primeArray[prime] = testNum
    
    print(prime)
print(primeArray[10000])

#CHANGE LINES 23 & 33 FOR WHATEVER PRIME YOU WANT TO FIND