class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return False

        stack = []

        brackets = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        for c in s:
            if c in brackets.values():
                stack.append(c)
            else:
                if not stack:
                    return False

                popped = stack.pop()

                if popped != brackets[c]:
                    return False
            
        
        return len(stack) == 0
                