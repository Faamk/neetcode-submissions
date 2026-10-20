class Solution:
    def isValid(self, s: str) -> bool:
        symbol_map = {'(':')',
                            '[':']',
                            '{':'}'}

        stack = []

        for c in s:
            if c in symbol_map:
                stack.append(symbol_map[c]) 
            else:
                if not stack or stack[-1] != c:
                    return False
                stack.pop()

        return not stack

        