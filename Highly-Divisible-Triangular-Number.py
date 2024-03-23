"""
Problem 12: Triangle number is sum of all numbers below and including itself. (i.e. 7th triangle num is 1+2+3...+7)
            What is the value of the first triangle number to have over five hundred factors?
Answer: 76576500
"""

def createTriangleNum(triangleCandidate: int) -> int:
    sum = 0
    for num in range(triangleCandidate+1):
        sum += num
    
    return sum
    
def findNumFactors(number: int) -> int:
    """
    Finds how many factors the number input has.

    :param number: Number to find number of factors of.
    :return: Returns the number of factors of the number input.
    """
    count = 0
    start = 1
    end = number
    while(start < end):
        if(number % start == 0):
            end = number / start
            if(start == end):
                count += 1
            else:
                count += 2
        
        start += 1
    
    return count
    
numFactors = 1
count = 1
while(numFactors <= 500):
    triangleNum = createTriangleNum(count)
    numFactors = findNumFactors(triangleNum)
    if(numFactors > 500):
        print(triangleNum)
    
    count += 1
        
