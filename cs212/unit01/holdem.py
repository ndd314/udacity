import random # this will be a useful library for shuffling
import itertools

def poker(hands):
    "Return a list of winning hands: poker([hand,...]) => [hand,...]"
    # find best 5 cards from 7 first
    besthands = [best_hand(hand) for hand in hands]
    return allmax(besthands, key=hand_rank)

def best_hand(hand):
    "From a 7-card hand, return the best 5 card hand."
    all_hands = itertools.combinations(hand, 5)
    return max(all_hands, key=hand_rank)

# for tie hands
def allmax(iterable, key=None):
    "Return a list of all items equal to the max of the iterable."
    max_hand = max(iterable, key=key)
    max_rank = hand_rank(max_hand)
    return [hand for hand in iterable if hand_rank(hand)==max_rank]

# looking table for rankings 0-10
# (5,) = five of a kind
# (4,1) = four of a kind
# (3,2) = full-house
count_rankings = {(5,):10, (4,1):7, (3,2):6, (3,1,1):3, (2,2,1):2, 
                  (2,1,1,1):1, (1,1,1,1,1):0}

def hand_rank(hand):
    groups = group(['--23456789TJQKA'.index(r) for r,s in hand])
    counts, ranks = unzip(groups)
    if ranks == (14,5,4,3,2): # handling ace-low straight
        ranks = (5,4,3,2,1)
    straight = len(ranks)==5 and max(ranks)-min(ranks)==4
    flush = len(ranks)==5 and len(set([s for r,s in hand]))==1
    return max(count_rankings[counts], 4*straight+5*flush), ranks
    # count_rankings can be 0,1,2,3,6,7,10
    # straight=4; flush=5; straight-flush=9

def group(items):
    "Return a list of [(count, x)...], highest count first, then highest x first."
    groups = [(items.count(x), x) for x in set(items)]
    return sorted(groups, reverse=True)

# return [(3,2,1), (4,5,6)] from [(3,4), (2,5), (1,6)] input
def unzip(pairs): return zip(*pairs)

unsort_deck = [r+s for r in '23456789TJQKA' for s in 'SHDC']

def deal(numhands, n=5, deck=unsort_deck):
    random.shuffle(deck)
    return [deck[n*i:n*(i+1)] for i in range(numhands)]

hand_names = {0:'High Card', 1:'One Pair', 2:'Two Pairs',
              3:'Three of a Kind', 4:'Straight', 5:'Flush', 6:'Full House',
              7:'Four of a Kind', 8:'Not a hand', 9:'Straigh Flush'}

# mathematical probability from wikipedia
hand_odds = {0:50.11, 1:42.25, 2:4.75, 3:2.11, 4:.39, 5:.196, 6:.140, 
             7:.024, 8:1., 9:.0015}
    
def hand_percentages(n=700*1000):
    counts = [0] * 10
    for i in range(n/10):
        for hand in deal(10):
            ranking = hand_rank(hand)[0]
            counts[ranking] += 1
    print_result(counts)

def print_result(counter):
    print "%20s: %8s %8s %-8s %-8s" % ('Hand Name', 'sim%', 'math%', 'sim',
        'math')
    for i, val in enumerate(counter):
        simprob = 100.*counter[i]/sum(counter)
        if simprob != 0:
            simodd = 100. / simprob
        else:
            simodd = 0
        print "%20s: %7.4f%% %7.4f%% 1:%-6i 1:%-6i" % (hand_names[i], 
            simprob, hand_odds[i], simodd, 100./hand_odds[i])

def test():
    hands = deal(10, 5)
    print hands
    winners = poker(hands)
    for winner in winners:
        print winner, hand_rank(winner) 

def deal_holdem(numhands, deck=unsort_deck):
    random.shuffle(deck)
    hands = [[deck[i], deck[numhands+i]] for i in range(numhands)]
    #burn1 numhands*2
    #flop numhands*2+1:numhands*2+4
    #burn2 numhands*2+4
    #turn numhands*2+5
    #burn3 numhands*2+6
    #river numhands*2+7
    pool = deck[numhands*2+1:numhands*2+4]
    pool.append(deck[numhands*2+5])
    pool.append(deck[numhands*2+7])
    hands.append(pool)
    return hands

def holdem(numhands=10):
    hands = deal_holdem(numhands)
    # create list of seven cards hands
    finalhands = []
    for i in range(numhands):
        #print 'Player %d %s' % (i, hands[i])
        finalhands.append(list(hands[i]+hands[numhands]))
    #print 'pool: %s' % (hands[numhands])
    winners = poker(finalhands)
    for winner in winners:
        wintype = hand_rank(winner)[0]
        #print 'winner: %s %s' % (list(winner), hand_names[wintype])
    return wintype

def holdem_percentages(numhands=10, rounds=1000):
    counts = [0]*10
    for i in range(numhands*rounds):
        counts[holdem(numhands)] += 1
    print_result(counts)

#hand_percentages()
holdem_percentages(10, 70000)
#holdem_percentages(10,10)