"""
Problem 17: If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used? 

Do not count spaces or hyphens. For example, 323 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
The use of "and" when writing out numbers is in compliance with British usage.
"""

def countLetters(string: str) -> int:
	"""
	Counts the letters in a string, disregarding spaces and hyphens.

	:param string: A string
	:return: Returns the number of letters in the parameter.
	"""
	return len(string.replace(" ", "").replace("-", ""))

def replaceLastInstance(string: str, old: str, new: str, occurrence: int = 1) -> str:
	"""
	Replaces the last instance of some substring 'old' in string with another substring 'new'.
	
	:param string: String to replace part of
	:param old: Substring to replace 
	:param new: Replacement substring
	:param occurrence: How many occurences of substring 'old' you want to replace with substring 'new' (Starts from back)
	"""
	
	return new.join(string.rsplit(old, occurrence))


def oneDigitNumbers(number: int) -> str:
    returnString = ""
    match number:
        case 1:
            returnString += "one"
        case 2:
            returnString += "two"
        case 3:
            returnString += "three"
        case 4:
            returnString += "four"
        case 5:
            returnString += "five"
        case 6:
            returnString += "six"
        case 7:
            returnString += "seven"
        case 8:
            returnString += "eight"
        case 9:
            returnString += "nine"
        case _:
            pass
        
    return returnString
    
def twoDigitNumbers(number: int) -> str:
    returnString = ""
    ones = number % 10
    tens = int(number / 10)
    
    match tens:
        case 1:
            match ones:
                case 0:
                    returnString += "ten"
                case 1:
                    returnString += "eleven"
                case 2:
                    returnString += "twelve"
                case 3:
                    returnString += "thirteen"
                case 4:
                    returnString += "fourteen"
                case 5:
                    returnString += "fifteen"
                case 6:
                    returnString += "sixteen"
                case 7:
                    returnString += "seventeen"
                case 8:
                    returnString += "eighteen"
                case 9:
                    returnString += "nineteen"
        
        case 2:
            returnString += "twenty-"
        case 3:
            returnString += "thirty-"
        case 4:
            returnString += "forty-"
        case 5:
            returnString += "fifty-"
        case 6:
            returnString += "sixty-"
        case 7:
            returnString += "seventy-"
        case 8:
            returnString += "eighty-"
        case 9:
            returnString += "ninety-"
        case _:
            pass
                    
    if(tens != 1):
        if(ones != 0):
            returnString += oneDigitNumbers(ones)
        else:
            returnString = returnString[:-1]
    
    return returnString

def threeDigitNumbers(number: int) -> str:
    returnString = ""
    hundreds = int(number / 100)
    lastTwoDigits = number % 100
    returnString += oneDigitNumbers(hundreds) + " hundred"
    if(lastTwoDigits != 0):
        returnString += " and " + twoDigitNumbers(lastTwoDigits)
    
    return returnString

def numAsString(number: int) -> str:
    returnString = ""
    numDigits = len(str(number))
    match numDigits:
        case 1:
            returnString += oneDigitNumbers(number)
        case 2:
            returnString += twoDigitNumbers(number)
        case 3:
            returnString += threeDigitNumbers(number)
        case 4:
            returnString += "one thousand"
        
    return returnString


length = 0
for i in range(1, 1001):
    length += countLetters(numAsString(i))
    
print(length)
    

#print(numAsString(1000) + " has " + str(countLetters(numAsString(1000))) + " letters.")


