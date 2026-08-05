class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        open_count = 0
        left_pass = ""

        for c in s:
            if c == "(":
                open_count += 1
            
            if c == ")":
                if open_count == 0:
                    continue
                else:
                    open_count -= 1


            left_pass += c
        
        close_count = 0
        right_pass = ""

        for c in left_pass[::-1]:
            if c == ")":
                close_count += 1

            if c == "(":
                if close_count == 0:
                    continue
                else:
                    close_count -= 1


            right_pass += c

        return right_pass[::-1]

