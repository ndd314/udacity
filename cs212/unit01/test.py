import itertools

black = [r+s for r in '23456789TJQKA' for s in 'SC'] 
red = [r+s for r in '23456789TJQKA' for s in 'DH'] 

def replacements(card):
    "find all possible hand with jokers"
    # use product function
    if card == '?B': return black
    elif card == '?R': return red
    else: return [card]
    
def best_wild_hand(hand):
    "Try all values for jokers in all 5-card selections."
    for h in itertools.product(*map(replacements,hand)):
        print h
    hands = set(best_hand(h) for h in itertools.product(*map(replacements,hand)))
    return max(hands, key=hand_rank)
    
def test_best_wild_hand():
    assert (sorted(best_wild_hand("6C 7C 8C 9C TC 5C ?B".split()))
            == ['7C', '8C', '9C', 'JC', 'TC'])
    assert (sorted(best_wild_hand("TD TC 5H 5C 7C ?R ?B".split()))
            == ['7C', 'TC', 'TD', 'TH', 'TS'])
    assert (sorted(best_wild_hand("JD TC TH 7C 7D 7S 7H".split()))
            == ['7C', '7D', '7H', '7S', 'JD'])
    return 'test_best_wild_hand passes'
    
print test_best_wild_hand()