"""
Problem 25: What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

Answer: 4782
"""

def fibonacciTillDigits(num: int) -> int:
    fibNum = 1
    fibAdd = 1
    fibDigits = len(str(fibAdd))
    index = 2
    while fibDigits < num:
        tempFib = fibNum
        fibNum = fibAdd
        fibAdd += tempFib
        index += 1
        fibDigits = len(str(fibAdd))
    
    return index

numDigits = int(input("Enter digit count: "))
print(fibonacciTillDigits(numDigits))


