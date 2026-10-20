class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []

        operations = {'+':(lambda x,y: x+y),'-':(lambda x,y: x-y),'*':(lambda x,y: x*y),'/':(lambda x,y: int(x/y))}
        
        for s in tokens:

            if s in operations:
                y = num_stack.pop()
                x = num_stack.pop()
                val = operations[s](x,y)
                num_stack.append(val)
            else:
                num_stack.append(int(s))

        print(num_stack)
        return num_stack[0]

