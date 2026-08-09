class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        hm = Counter(hand)
        dq = deque([])
        

        for i, card in enumerate(sorted(hm.keys())):
            count = hm[card]

            if count < len(dq):
                return False

            while count > len(dq): 
                dq.append((card, i))

            while count > 0 and count == len(dq):
                if card - dq[0][0] == groupSize - 1 and i - dq[0][1] == groupSize - 1:
                    dq.popleft()
                    count -= 1
                else: break

        return len(dq) == 0
                
            