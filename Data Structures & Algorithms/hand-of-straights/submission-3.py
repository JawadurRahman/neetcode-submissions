class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hm = Counter(hand)
        hand.sort()

        for card in hand:
            if hm[card] > 0:
                for c2 in range(card, card + groupSize):
                    if hm[c2] == 0: return False
                    hm[c2] -= 1
        return True
                
            