"""
Problem 4: Find the largest palindrome made from the product of two 3-digit numbers.
"""

def isPalindrome(number):
	num = str(number)
	palindrome = True
	for i in range(len(num)-1):
		j = len(num)-i-1
		if(num[i] == num[j] and palindrome is True):
			palindrome = True
		else:
			palindrome = False
			return palindrome
	return palindrome

upTo, highestPalindrome = int(input("Enter upper boundary: ")), 0
for i in range(upTo + 1):
	for j in range(upTo + 1):
		if(isPalindrome(i * j) is True and (i * j) > highestPalindrome):
			highestPalindrome = i * j

print(highestPalindrome)