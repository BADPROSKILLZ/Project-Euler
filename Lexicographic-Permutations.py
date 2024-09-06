"""
Problem 24: 

A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
012   021   102   120   201   210
What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

Answer: 2783915460
"""
import time

def makeAnagrams(start: str, end: str, anagrams: list[str]) -> None:
    if(len(end) == 0):
        anagrams.append(start + end)
    else:
        for i in range(len(end)):
            newStart = start + end[i]
            newEnd = end[:i] + end[i+1:]
            makeAnagrams(newStart, newEnd, anagrams)

anagrams = []
start = ""
end = input("Enter a word: ")
makeAnagrams(start, end, anagrams)
list(set(anagrams)).sort() #OK so list->set->list works really well to get rid of duplicates; 10000+ times quicker than previous implementation
#print(anagrams)

try:
    print(anagrams[999999])
except:
    print("Not enough anagrams")

print(time.process_time())