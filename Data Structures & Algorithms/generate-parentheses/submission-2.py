class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        all_strs = []

        def backtrack(n_open,n_close,current_str=[]):
            if not n_open and not n_close:
                all_strs.append("".join(current_str))
            
            if n_open:
                current_str.append('(')
                backtrack(n_open-1,n_close,current_str)
                current_str.pop()
            
            if n_close > n_open:
                current_str.append(')')
                backtrack(n_open,n_close-1,current_str)
                current_str.pop()

        backtrack(n,n,[])
        return all_strs
