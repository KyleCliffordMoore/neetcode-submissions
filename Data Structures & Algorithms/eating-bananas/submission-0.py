class Solution:

    def validSolution(self, piles, h, k):

        if k == 0:
            return False if sum(piles) > 0 else True
            
        hcount = h
        for pile in piles:
            hcount -= math.ceil(pile / k) 
        return True if hcount >= 0 else False

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        rk = sum(piles)
        lk = 0

        k = lk

        while lk <= rk:
            midk = (lk + rk) // 2
            isValid = self.validSolution(piles, h, midk)
            print(midk, isValid)
            if isValid:
                k = midk
                rk = midk - 1
            else:
                lk = midk + 1

        return k