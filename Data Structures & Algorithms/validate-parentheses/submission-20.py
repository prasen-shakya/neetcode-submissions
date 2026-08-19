class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        open = {'(', '[', '{'}
        close_to_open = {')':'(', ']':'[', '}':'{'}

        for c in s:
            if c in open:
                stack.append(c)
                continue
            
            if stack and stack[-1] == close_to_open[c]:
                stack.pop()
            else:
                return False
            
        return len(stack) == 0
