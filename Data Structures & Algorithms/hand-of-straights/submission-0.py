class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        count = {}
        for n in hand:
            count[n] = 1 + count.get(n, 0)
        hand.sort()
        for n in hand:
            if count[n] == 0:
                continue
            for i in range(n, n+groupSize):
                if count.get(i, 0) <= 0:
                    return False
                count[i] -= 1
        return True

        
        