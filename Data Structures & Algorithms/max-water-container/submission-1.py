class Solution:
    def maxArea(self, heights: List[int]) -> int:
        idx_a = 0
        idx_b = len(heights) - 1
        max_size = 0

        while idx_b > idx_a:
            current_size = min(heights[idx_a],heights[idx_b]) * (idx_b-idx_a)
            max_size = max(max_size,current_size)

            if heights[idx_a] < heights[idx_b]:
                idx_a += 1
            else:
                idx_b -=1

        return max_size