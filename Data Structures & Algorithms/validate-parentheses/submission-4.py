class Solution:
    def isValid(self, s: str) -> bool:
        symbol_map_open = {'(':'P',
                            '[':'B',
                            '{':'C'}
        symbol_map_close = {')':'P',
                            ']':'B',
                            '}':'C'}
        symbol_map = symbol_map_open | symbol_map_close

        stack = []

        for c in s:
            current_key = symbol_map[c]
            if c in symbol_map_open.keys():
                stack.append(current_key) 
            elif c in symbol_map_close.keys():
                if not stack or stack[-1] != current_key:
                    return False
                stack.pop()

        return not stack

        