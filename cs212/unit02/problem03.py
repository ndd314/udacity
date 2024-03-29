# --------------
# User Instructions
#
# Write a function, longest_subpalindrome_slice(text) that takes 
# a string as input and returns the i and j indices that 
# correspond to the beginning and end indices of the longest 
# palindrome in the string. 
#
# Grading Notes:
# 
# You will only be marked correct if your function runs 
# efficiently enough. We will be measuring efficency by counting
# the number of times you access each string. That count must be
# below a certain threshold to be marked correct.
#
# Please do not use regular expressions to solve this quiz!



def palindrome(text):
    return text==text[::-1]

def longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    text = text.upper()
    if text=='': return (0,0)
    for start, end in longest_subtext(text):
        #print subtext
        return (start,end) 

def longest_subtext(text):
    rev = text[::-1]
    lenmax = len(text)
    for longest in range(lenmax,0,-1):
        for start in range(lenmax-longest+1):
            subtext = text[start:start+longest]
            subtext2 = rev[lenmax-(longest+start):lenmax-start]
            print subtext + '--' + subtext2
            if subtext==subtext2:
                yield (start,start+longest)

def test():
    L = longest_subpalindrome_slice
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    assert L('Race carr') == (7, 9)
    assert L('') == (0, 0)
    assert L('something rac e car going') == (8,21)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    return 'tests pass'

#print longest_subtext('racecar')
print test()