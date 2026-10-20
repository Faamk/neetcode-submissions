class Solution:
    def trap(self, height: List[int]) -> int:

        if not height:
             return 0
        idx_a = 0
        idx_b =len(height) - 1

        max_a = height[idx_a]
        max_b = height[idx_b]

        result = 0
        while idx_a < idx_b:
            if max_a < max_b:
                idx_a += 1
                max_a = max(max_a, height[idx_a])
                result += max_a - height[idx_a]
            else:
                idx_b -= 1
                max_b = max(max_b, height[idx_b])
                result += max_b -height[idx_b]

        return result
        