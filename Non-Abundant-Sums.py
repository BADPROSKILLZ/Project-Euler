"""
Problem 23: Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
For example, the sum of the proper divisors of 28 would be 1+2+4+7+14=28, which means that 28 is a perfect number.
A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this 
sum exceeds n.

As 12 is the smallest abundant number, 1+2+3+4+6=16, the smallest number that can be written as the sum of two 
abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be 
written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis 
even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers 
is less than this limit.

Answer: 
"""

def numberIdentifier(num: int) -> bool:
    sum = 0
    divisors = []
    for i in range(1, num):
        if(num % i == 0 and i not in divisors):
            sum += i
            divisors.append(i)
        
    if sum > num:
        return True

abundantList = []

for i in range(1, 28123):
    if numberIdentifier(i):
        abundantList.append(i)

combinables = [0]*28124
for i in range(len(abundantList)):
    for j in range(i, len(abundantList)):
        if abundantList[i] + abundantList[j] < 28123 and combinables[abundantList[i] + abundantList[j]] == 0:
            combinables[abundantList[i] + abundantList[j]] = abundantList[i] + abundantList[j]
            
sumOfNonCombinables = 0
for i in range(len(combinables)):
    if combinables[i] == 0:
        sumOfNonCombinables += i

print(sumOfNonCombinables)

#print(abundantList)
