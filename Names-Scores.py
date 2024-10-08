"""
Problem 22: What is the total of all the name scores in the file?

Using names.txt, a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this 
value by its alphabetical position in the list to obtain a name score.
For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 54,
is the 938th name in the list. So, COLIN would obtain a score of 938 * 53 = 49714.

Answer: 871198282
"""

with open('C:/Users/Braden/Downloads/names.txt', 'r') as f:
    names = f.read()

nameList = names.split("\",\"")
nameList[-1] = nameList[-1].replace("\"", "")
nameList[0] = nameList[0].replace("\"", "")
nameList.sort()
#print(nameList)

charScores = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 
              'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21,
              'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
print(charScores.values())

fileScore = 0
nameScore = 0
for name in nameList:
    nameScore = 0
    for char in name:
        nameScore += charScores.get(str(char))
        print(nameScore)
    fileScore += nameScore * int(nameList.index(name) + 1)

print(fileScore)