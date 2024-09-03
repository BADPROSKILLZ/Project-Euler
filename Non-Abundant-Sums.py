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

Answer: 4179871 #Took 5 Minutes, could be optimized further
"""
import time
def numberClassifier(num: int):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
            #print(i, " ", sum)
    
    if sum > num: return "a"
    elif sum < num: return "d"
    else: return "p"


abundantList = []
deficientList = []
perfectList = []
addedAbundant = []
allNums = []
sum = 0

        #userInput = int(input("Enter a number: "))
        #print(numberClassifier(userInput))

for num in range(28123):
    if numberClassifier(num) == "a":
        abundantList.append(num)
    elif numberClassifier(num) == "d":
        deficientList.append(num)
    else: 
        perfectList.append(num)
    
allNums += abundantList + deficientList + perfectList

for i in range(len(abundantList)):
    for j in range(i, len(abundantList)):
        if(abundantList[i]+abundantList[j]<=28123):
            addedAbundant.append(abundantList[i] + abundantList[j])

for addedNum in addedAbundant:
    while allNums.count(addedNum) > 0:
        allNums.remove(addedNum)

for num in allNums:
    sum += num

print(sum)
#print(abundantList, "a")
#print(perfectList, "p")
#print(deficientList, "d")
print(time.process_time())