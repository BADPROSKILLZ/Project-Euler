"""
Problem 15: How many routes are there to the bottom right corner from the upper left corner of a 20 x 20 square? Only go right and down.
Answer: 137846528820
"""

def factorial(number: int) -> int:
    product = 1
    for num in range(1, number+1):
        product *= num
    
    return product

size = 0
while(size != -1):
    try:
        size = int(input("Enter the size of the grid; -1 to exit "))
    except:
        print("Not an integer. ")
        quit()
        
    numPaths = int(factorial(size * 2) / (factorial(size) ** 2))
    print(f"The number of paths of a {size}x{size} grid is {numPaths}.")