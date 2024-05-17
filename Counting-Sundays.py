"""
Problem 19: You are given the following information:
    * 1 Jan 1900 was a Monday.
    * Thirty days has September,
    * April, June and November.
    * All the rest have thirty-one,
    * Saving February alone,
    * Which has twenty-eight, rain or shine.
    * And on leap years, twenty-nine.
    * A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""
def numDaysInMonth(month: int = 1, year: int = 1900) -> int:
    leapYear = False
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):                                                                                                                                                                                                                                                                   
        leapYear = True

    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        if leapYear:
            return 29
        else:
            return 28

def firstOfTheMonth(month: int, year: int) -> str:
    firstDay = 1 #Monday
    for yr in range(1900, year+1):
        for mnth in range(1, month):
            firstDay += numDaysInMonth(mnth, yr) % 7 #Weekday increased
            firstDay = (firstDay % 7 if firstDay != 7 else 7) #Fixes number being greater than 7
    
    match firstDay:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _:
            pass


numSundays = 0
for yr in range(1901, 2001):
    for mnth in range(1, 13):
        if firstOfTheMonth(mnth, yr) == "Sunday":
            numSundays += 1
        
print(numSundays) #NOT YET WORKING
            