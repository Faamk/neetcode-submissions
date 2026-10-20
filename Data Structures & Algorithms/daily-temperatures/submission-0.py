class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for t in temperatures]
        stack = []
        print(result[0])
        for i,temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                index = stack[-1]
                result[index] = i-index
                stack.pop()
            stack.append(i)
        
        return result
