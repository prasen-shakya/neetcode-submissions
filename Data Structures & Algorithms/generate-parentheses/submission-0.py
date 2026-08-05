class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(current: str, start: int, end: int):
            if start == end == n:
                res.append(current)
                return 
            
            if start < n:
                backtrack(current + "(", start + 1, end)
            if end < start:
                backtrack(current + ")", start, end + 1)


        backtrack("", 0, 0)
        return res