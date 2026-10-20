class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right = max(piles)
        left = 1
        k = right

        while left <= right:
            time_to_eat = 0
            middle = (left + right) // 2
            for pile in piles:
                time_to_eat += math.ceil(pile/middle)
            if time_to_eat <= h:
                k = min(k,middle)
                right = middle - 1
            if time_to_eat > h:
                left = middle + 1

        return k

         
