"""
Problem 26: Find the value of d < 1000 for which 1/d contains the longest recurring 
cycle in its decimal fraction part.

Answer: 
"""
from decimal import *

getcontext().prec = 4096

def replaceLastInstance(string: str, old: str, new: str, occurrence: int = 1) -> str:
	"""
	Replaces the last instance of some substring 'old' in string with another substring 'new'.
	
	:param string: String to replace part of
	:param old: Substring to replace 
	:param new: Replacement substring
	:param occurrence: How many occurences of substring 'old' you want to replace with substring 'new' (Starts from back)
	"""
	
	return new.join(string.rsplit(old, occurrence))

def findCycle(num: int) -> list[int]:
    longestReciprocalLength = 0
    longestCycleGenerator = 0
    longestReciprocal = 0
    for i in range(2, num+1):
        reciprocal = Decimal(1)/Decimal(i)
        reciprocal = str(reciprocal).replace("0.", "", )
        if len(reciprocal) >= 4096:
            reciprocal = reciprocal[0:len(reciprocal)-1]
            
        #print(reciprocal, detectDuplicates(reciprocal))
        cycle = detectDuplicates(reciprocal) 
        if cycle != "No Cycle" and len(cycle) > longestReciprocalLength:
            longestReciprocalLength = len(cycle)
            longestCycleGenerator = i
            longestReciprocal = int(cycle)
    
    return [longestCycleGenerator, longestReciprocalLength, longestReciprocal]


def detectDuplicates(string: str) -> str:
    for num in range(len(string)):
        try:
            #Same repeating digit
            if string[num] == string[num+1] and string.count(string[num]) == len(string) - num:
                return string[num]
        except:
            pass
            
        for i in range(1, len(string) - num):
            try:
                #Same repeating digits
                if string[num:num+i] == string[num+i+1:num+2*i+1] == string[num+2*i+2:num+3*i+2]:
                    return string[num:num+i+1]
            except:
                continue
    return "No Cycle"

userInput = int(input("Enter upper limit: "))
arr = findCycle(userInput)
print("The longest reciprocal is made by the number "+str(arr[0])+".")
print("The size of the longest reciprocal is "+str(arr[1])+".")
print("The longest reciprocal is "+str(arr[2])+".")
