"""
Problem 9: Pythagorean Triplet means a<b<c and a^2 + b^2 = c^2. There exists exactly one Pythagorean triplet for which a+b+c=1000. 
           Find the product of abc.
Answer: 31875000
"""

def checkPythagoreanTriplet(a: int, b: int, c: int) -> bool:
    """
    Checks if the 3 numbers input make a pythagorean triplet.
    
    :param a: The smallest number in the triplet.
    :param b: The middlest number in the triplet.
    :param c: The largest number in the triplet.
    :return: Returns true if the parameters make a pythagorean triplet, false if not.
    """
    if(a < b and b < c):
        if(a ** 2 + b ** 2 == c ** 2):
            return True
        
    return False

for a in range(1000):
    for b in range(a +1, 1000):
        for c in range(b + 1, 1000):
            if(checkPythagoreanTriplet(a, b, c) and a+b+c == 1000):
                print(a*b*c)
                quit()

