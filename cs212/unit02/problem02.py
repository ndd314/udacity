#------------------
# User Instructions
#
# Hopper, Kay, Liskov, Perlis, and Ritchie live on 
# different floors of a five-floor apartment building. 
#
# Hopper does not live on the top floor. 
# Kay does not live on the bottom floor. 
# Liskov does not live on either the top or the bottom floor. 
# Perlis lives on a higher floor than does Kay. 
# Ritchie does not live on a floor adjacent to Liskov's. 
# Liskov does not live on a floor adjacent to Kay's. 
# 
# Where does everyone live?  
# 
# Write a function floor_puzzle() that returns a list of
# five floor numbers denoting the floor of Hopper, Kay, 
# Liskov, Perlis, and Ritchie.

import itertools

def adjacent(f1, f2):
    return abs(f1-f2)==1

def higher(f1, f2):
    return f1>f2

def floor_puzzle():
    floors = bottom, _, _, _, top = [ 1, 2, 3, 4, 5 ]
    orderings = list(itertools.permutations(floors))
    return list(next((Hopper, Kay, Liskov, Perlis, Ritchie)
        for (Hopper, Kay, Liskov, Perlis, Ritchie) in orderings
        if not Hopper is top 
        and not Kay is bottom 
        and not (Liskov is top or Liskov is bottom)
        and higher(Perlis, Kay) 
        and not adjacent(Ritchie, Liskov)
        and not adjacent(Liskov, Kay)))

print floor_puzzle()
