class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == '(':
                stack.append('P')
            elif c == '[':
                stack.append('B')
            elif c == '{':
                stack.append('C')    


            elif c == ')':
                if not stack or stack[-1] != 'P':
                    return False
                stack.pop()
            elif c == ']':
                if not stack or stack[-1] != 'B':
                    return False
                stack.pop()
            elif c == '}':
                if not stack or stack[-1] != 'C':
                    return False
                stack.pop()

        return not stack

        