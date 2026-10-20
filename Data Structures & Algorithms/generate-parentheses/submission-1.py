class Solution:
    p_map = {'(':')'}

    def generateParenthesis(self, n: int) -> List[str]:
        self.combos = []
        self.generateParenthesis_child(n,n)
        return self.combos
    
    def generateParenthesis_child(self, n_open: int,  n_close: int, current_string =[], current_stack = []) -> List[str]:
        if not n_open and not n_close:
            print(current_stack)
            self.combos.append(''.join(current_string))

        if current_stack and n_close and current_stack[-1] == '(':
            current_string.append(')')
            current_stack.pop()
            print(f'call self.generateParenthesis_child({n_open},{n_close-1},{current_string},{current_stack})')
            self.generateParenthesis_child(n_open,n_close-1,current_string,current_stack)
            current_string.pop()
            current_stack.append('(')

        if n_open:
            current_stack.append('(')
            current_string.append('(')
            print(f'call self.generateParenthesis_child({n_open-1},{n_close},{current_string},{current_stack})')
            self.generateParenthesis_child(n_open-1,n_close,current_string,current_stack)
            current_string.pop()
            current_stack.pop()



            

        