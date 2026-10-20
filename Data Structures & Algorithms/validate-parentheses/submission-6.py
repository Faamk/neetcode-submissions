class Solution:
    symbol_map = {  '(':')',
                    '[':']',
                    '{':'}'}
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c in self.symbol_map:
                stack.append(self.symbol_map[c]) 
            else:
                if not stack or stack[-1] != c:
                    return False
                stack.pop()

        return not stack

        