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
    string = string.replace(" ", "").replace("-", "")
    return len(string)

def replaceLastInstance(s, old, new, occurrence):
     li = s.rsplit(old, occurrence)
     return new.join(li)

def stringifyNum(number: int) -> str:
    returnString = ""
    numString = str(number)
    for char in numString:
        numLength = len(numString)
        match char:
            case "1":
                returnString += "one "
                match numLength:
                    case 1:
                        if(numString[char == 0]):
                            returnString += "thousand "
                        if(numString[char == 2] and numString["1" == numString.index(char)+1]):
                            returnString.replace("one", "ten", -1)
                    case 2:

                    case 3:

                    case 4:
                
            
            case "2":
                returnString += "two "

            case "3":
                returnString += "three "

            case "4":
                returnString += "four "

            case "5":
                returnString += "five "
            
            case "6":
                returnString += "six "

            case "7":
                returnString += "seven "

            case "8":
                returnString += "eight "

            case "9":
                returnString += "nine "

    return returnString

print(stringifyNum(1))