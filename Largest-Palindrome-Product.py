"""
Problem 4: Find the largest palindrome made from the product of two 3-digit numbers.
Answer: 906609
"""

def isPalindrome(palindromeCandidate: int) -> bool:
	"""
	Checks if a number is a palindrome
	
	:param palindromeCandidate: Number to check palindromic status of.
	:return: Returns true if the number is a palindrome, false otherwise.
	"""
	
	numString = str(palindromeCandidate)
	palindrome = True
	for num in range(len(numString)-1):
		inverseNum = len(numString)-num-1
		if(numString[num] == numString[inverseNum] and palindrome is True):
			palindrome = True
		else:
			return False
	return palindrome

upTo, highestPalindrome = int(input("Enter upper boundary: ")), 0
for i in range(upTo + 1):
	for j in range(upTo + 1):
		if(isPalindrome(i * j) is True and (i * j) > highestPalindrome):
			highestPalindrome = i * j

print(highestPalindrome)