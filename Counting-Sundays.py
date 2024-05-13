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

def numDaysIn20thCentury() -> int:
    sumDays = 7 * 31
    sumDays += 30*4
    sumDays += 28
    sumDays *= 100
    for yr in range(1901, 2001):
        if(yr % 4 == 0):
            sumDays += 1
    
    return sumDays

numSundays = int((numDaysIn20thCentury() - 6) / 7)
sundaysTheFirst = numSundays / 6
print(sundaysTheFirst)