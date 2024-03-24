"""
Problem 14: Which starting number, under one million, produces the longest chain? (If odd, 3x +1; if even, x/2)
Answer: 837799
"""

def findCollatzSequence(number: int) -> int:
    """
    Returns the length of a number's collatz sequence.
    
    :param number: The number to find the length of the collatz sequence of.
    :return: Returns the length of a number's collatz sequence.
    """
    count = 1
    
    while(number != 1):
        count += 1
        #print(number, end=" ")
        if(number % 2 == 0): #even
            number = int(number / 2)
        else:
            number = 3 * number + 1
        
        
    #print(1)
    #print("\n")
    return count

longestChain = 0
currentChain = 0
longestChainNum = 0
for num in range(1, 1_000_000+1):
    currentChain = findCollatzSequence(num)
    if(currentChain > longestChain):
        longestChain = currentChain
        longestChainNum = num
    
    print(f"Longest chain: {longestChain, num}")
    
print(longestChainNum)
        