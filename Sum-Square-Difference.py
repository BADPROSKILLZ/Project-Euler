"""
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def squareSum(highestNum: int = 100) -> int:
    sum = 0
    for num in range(1, highestNum+1):
        sum += num
    
    return (sum ** 2)

def sumOfSquares(highestNum: int = 100) -> int:
    sum = 0
    for num in range(1, highestNum+1):
        sum += num ** 2
    
    return sum

userNum = 0
while(userNum != -1):
    try:
        userNum = int(input("Enter a number; -1 to exit "))
    except:
        print("Not an integer. ")
        quit()
        
    print(f"The difference between the square of the sum and the sum of the squares is {squareSum(userNum) - sumOfSquares(userNum)}.\n")