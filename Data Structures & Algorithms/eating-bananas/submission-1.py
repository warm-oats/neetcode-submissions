class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort() # Sort in non-descending order to prepare for binary search

        start_k, end_k = 1, max(piles)
        min_k = None

        while end_k >= start_k:
            middle_k = math.floor((start_k + end_k) / 2)
            eat_hours = 0

            for pile in piles:
                eat_hours += math.ceil(pile / middle_k)
            
            if eat_hours > h:
                start_k = middle_k + 1
            else:
                end_k = middle_k - 1
                min_k = middle_k if not min_k else min(min_k,middle_k)
        
        return min_k

