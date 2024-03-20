def primeCheck(primeCandidate: int) -> bool:
    isPrime = True
    for num in range(3, int(primeCandidate / 2)): #Check only first half, rest will be covered automatically
        if (primeCandidate % num == 0): #Check if num is a factor
            return False
    
    return isPrime


primeCandidate = int(input("Enter a number: "))
greatestFactor = 1
upperBound = primeCandidate
for possibleFactor in range(upperBound):
    if (possibleFactor <= upperBound):
        possibleFactor += 1
        if ((primeCandidate / possibleFactor) % 1 != 0):
            continue

        upperBound = primeCandidate / possibleFactor
        print(possibleFactor, primeCheck(possibleFactor), upperBound, primeCheck(upperBound))

quit()
